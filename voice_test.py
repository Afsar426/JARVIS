import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init('nsss')  # For macOS ('sapi5' for Windows, 'espeak' for Linux)

# List all available voices on your system
voices = engine.getProperty('voices')

print("Available Voices:")
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name} ({voice.id})")

# Ask user to choose a voice number
choice = int(input("\nEnter the number of the voice you want to test: "))

# Set the chosen voice
engine.setProperty('voice', voices[choice].id)

# Adjust speed and volume
engine.setProperty('rate', 165)   # 150–180 = clear, natural pace
engine.setProperty('volume', 1.0) # 0.0 to 1.0

# Test message
test_message = "Hello Afsar, I am your upgraded Jarvis assistant. How do I sound?"

# Speak the test message
print(f"\nTesting voice: {voices[choice].name}")
engine.say(test_message)
engine.runAndWait()