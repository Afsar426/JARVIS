🧠 MyJarvis – Your Personal AI Voice Assistant

MyJarvis is a powerful, offline-capable AI-based virtual assistant built with Python. It performs day-to-day tasks like opening applications, searching the web, reading emails, playing music, and speaking responses — all through voice commands.

⸻

🚀 Features

✅ Voice Recognition – Understands spoken commands using speech_recognition.
✅ Text-to-Speech (TTS) – Speaks responses naturally with pyttsx3.
✅ Automation Tasks – Opens apps, websites, and files via voice.
✅ Information Retrieval – Searches Google, Wikipedia, or YouTube directly.
✅ System Control – Manage files, take screenshots, check battery, etc.
✅ Email Functionality – Sends or reads emails with simple voice prompts.
✅ Modular Design – Easy to expand and integrate with APIs.

🛠️ Tech Stack
Component
Technology
Programming Language
Python 3.x
Voice Input
speech_recognition
Voice Output
pyttsx3
Web Automation
webbrowser, os, subprocess
Email Handling
smtplib, imaplib
Optional APIs
OpenAI, Wikipedia, Weather API

📦 Installation

1️⃣ Clone the Repository
git clone https://github.com/Afsar426/JARVIS.git
cd JARVIS
2️⃣ Install Dependencies

Make sure you have Python 3.8+ installed. Then run:
pip install -r requirements.txt
If there’s no requirements.txt, install manually:
pip install pyttsx3 speechrecognition pyaudio wikipedia requests pyautogui

▶️ Usage

Run the assistant using:
python run.py
Or if your main file is main.py:
python main.py

Once started, MyJarvis will greet you and start listening for voice commands.

Example commands:
	•	“Open YouTube”
	•	“Play music”
	•	“Send an email”
	•	“Search Wikipedia for Artificial Intelligence”
	•	“What’s the time?”
	•	“Exit Jarvis”

⸻

⚙️ Configuration

You can customize:
	•	Voice and Speed: Inside your code (via pyttsx3 settings)
	•	Email setup: Add your Gmail credentials in the configuration file or environment variables
	•	Command list: Modify command.py or task.py to add new voice functions

⸻

🧩 Folder Structure
MyJarvis/
│
├── engine/
│   ├── command.py       # Core commands logic
│   ├── speak.py         # Text-to-speech module
│   └── listener.py      # Voice recognition module
│
├── assets/              # Audio or image assets
├── run.py               # Main executable file
├── requirements.txt     # Dependencies
└── README.md            # Project documentation

🧠 How It Works
	1.	Speech Input: User gives a command through a microphone.
	2.	Command Recognition: speech_recognition converts it to text.
	3.	Processing: Command is matched to internal logic or APIs.
	4.	Action Execution: Jarvis performs the task (open app, speak, etc.).
	5.	Speech Output: pyttsx3 converts the result back to voice.

⸻

🔒 Security Notes
	•	Do not hardcode your Gmail password or API keys.
	•	Use environment variables (.env) for sensitive credentials.
	•	Avoid executing unknown system commands directly from voice input.

⸻

🧑‍💻 Author

👤 Afsar Azam
B.Tech (AI) – Sage University, Indore
Frontend Developer | AI & Data Analysis Enthusiast

📧 afsarazam404@gmail.com
🌐 GitHub: Afsar426

⸻

🌟 Future Enhancements
	•	Integration with OpenAI GPT API for natural conversations
	•	Smart home automation
	•	Personalized reminders & task scheduling
	•	GUI dashboard for monitoring actions

⸻
