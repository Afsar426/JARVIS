import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    text = str(text)
    import platform
    if platform.system() == "Windows":
        engine = pyttsx3.init('sapi5')
    elif platform.system() == "Darwin":
        engine = pyttsx3.init('nsss')
    else:
        engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[4].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    r.energy_threshold = 300  # Adjust sensitivity for better noise handling
    r.pause_threshold = 0.8   # Slightly increase pause threshold for better phrase detection

    for attempt in range(2):  # Retry up to 2 times on failure
        try:
            with sr.Microphone() as source:
                print('listening....')
                eel.DisplayMessage('listening....')
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, 10, 6)

            print('recognizing')
            eel.DisplayMessage('recognizing....')
            query = r.recognize_google(audio, language='en-us')  # Changed to US English for potentially better accuracy
            print(f"user said: {query}")
            eel.DisplayMessage(query)
            time.sleep(2)
            return query.lower()
        except Exception as e:
            if attempt == 0:
                speak("Sorry, I didn't catch that. Please try again.")
            else:
                speak("Recognition failed after retries.")
                return ""

    return ""


@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if contact_no != 0:
                speak("Which mode you want to use — WhatsApp or mobile?")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query:
                        speak("What message to send?")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("Please try again")
                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("What message to send?")
                        query = takecommand()
                    elif "phone call" in query:
                        message = 'call'
                    else:
                        message = 'video call'

                    whatsApp(contact_no, query, message, name)

        elif "read my emails" in query:
            from engine.features import read_emails
            read_emails(max_emails=5)

        elif "send email" in query:
            speak("Please provide recipient email address")
            to_email = takecommand()
            if not to_email:
                speak("No email address provided. Cancelling.")
                return
            speak("What is the subject?")
            subject = takecommand()
            if not subject:
                speak("No subject provided. Cancelling.")
                return
            speak("What is the message?")
            message_text = takecommand()
            if not message_text:
                speak("No message provided. Cancelling.")
                return
            from engine.features import send_email
            send_email(to_email, subject, message_text)

        else:
            from engine.features import geminai
            geminai(query)

    except Exception as e:
        print("error:", e)

    eel.ShowHood()