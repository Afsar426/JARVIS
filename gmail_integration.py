import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
from engine.command import speak  # Your existing speak function

# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.send']

TOKEN_PATH = 'token.json'
CREDENTIALS_PATH = 'credentials.json'

# Authenticate Gmail API
def authenticate_gmail():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        speak("Please visit the authorization URL in the console to authenticate Gmail.")
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
        speak("Gmail authentication successful.")
    return creds

# Read Emails
def read_emails(max_emails=5):
    try:
        creds = authenticate_gmail()
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me', maxResults=max_emails).execute()
        messages = results.get('messages', [])

        if not messages:
            speak("No new emails found.")
            return

        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
            subject = None
            sender = None
            body = ""
            for header in msg_data['payload']['headers']:
                if header['name'] == 'From':
                    sender = header['value']
                if header['name'] == 'Subject':
                    subject = header['value']
            if 'parts' in msg_data['payload']:
                for part in msg_data['payload']['parts']:
                    if part['mimeType'] == 'text/plain':
                        body = base64.urlsafe_b64decode(part['body']['data']).decode()
            else:
                body = base64.urlsafe_b64decode(msg_data['payload']['body']['data']).decode()

            speak(f"Email from {sender} with subject {subject}.")
            print(f"From: {sender}\nSubject: {subject}\nBody: {body[:100]}...\n---")  # First 100 chars

    except HttpError as error:
        print(f'An error occurred: {error}')

# Send Email
def send_email(to_email, subject, message_text):
    try:
        creds = authenticate_gmail()
        service = build('gmail', 'v1', credentials=creds)

        message = MIMEText(message_text)
        message['to'] = to_email
        message['subject'] = subject

        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        message_body = {'raw': raw_message}

        sent_message = service.users().messages().send(userId='me', body=message_body).execute()
        speak(f"Email sent to {to_email} successfully.")
        print(f"Message ID: {sent_message['id']}")
    except HttpError as error:
        print(f'An error occurred: {error}')