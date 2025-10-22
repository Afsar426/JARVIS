import os
import eel
import platform
import subprocess

from engine.features import *
from engine.command import *
from engine.auth import recoganize

def start():
    eel.init("www")
    playAssistantSound()

    @eel.expose
    def init():
        # Use device.sh for macOS/Linux, device.bat for Windows
        if platform.system() == "Windows":
            subprocess.call([r'device.bat'])
        else:
            subprocess.call(['bash', 'device.sh'])
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can i Help You")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")
    # Launch browser (Edge on Windows, default on macOS)
    if platform.system() == "Windows":
        os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    else:
        os.system('open http://localhost:8000/index.html')

    eel.start('index.html', mode=None, host='localhost', block=True)