import time
import webbrowser
import keyboard
import mouse
from playsound import playsound  # Add this for playing sound

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

page_link = input("Provide THe PAge Link:\n")
webbrowser.open(page_link)
time.sleep(3)

mouse.click("left")
time.sleep(1)

keyboard.press("Ctrl + F")
playsound('assets/sound/alert.mp3')  # Plays a sound when aborting
