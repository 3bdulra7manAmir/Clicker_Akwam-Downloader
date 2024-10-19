import time
import mouse
import keyboard
import pyautogui
import emoji
from playsound import playsound

# emoji_text = emoji.emojize(":winking_face:")
# emoji_text_ghost = emoji.emojize(":ghost:")

# emoji_text_robot = emoji.emojize(":robot:")
# print(f"Welcome to Akwam Series Downloader {emoji_text_robot}\n")
#
# series_link = input("Enter Your Series Link: ")
# print(f"Thanks {emoji_text_robot},\tYour Link is: {series_link}\n")
#
# counter = input(f"Enter Your Episodes Count {emoji_text_robot}: ")
# print(f"Episodes Count is: {counter}\n")

pyautogui.FAILSAFE = True
ender = True
counter = 1


def downloader():
    global counter
    global ender
    while ender:
        time.sleep(3)

        # MB Btn
        mouse.move(x=1155, y=905)
        mouse.click("left")

        time.sleep(7)

        # Click Here Btn
        mouse.move(x=1216, y=830)
        mouse.click("left")

        time.sleep(7)

        # Download Btn
        mouse.move(x=955, y=915)
        mouse.click("left")

        time.sleep(10)

        # Change IDM Save Folder
        mouse.move(x=857, y=450)
        time.sleep(2)

        mouse.click("left")
        time.sleep(2)

        # Scroll To Change it To Home Downloads
        pyautogui.scroll(800)
        time.sleep(2)

        # Move To The Start Download Btn
        mouse.move(x=946, y=624)
        time.sleep(2)
        mouse.click("left")
        time.sleep(5)

        # Minimize Btn
        mouse.move(x=1100, y=355)
        time.sleep(2)
        mouse.click("left")

        # Left Click To Select The Browser Page
        time.sleep(2)
        mouse.click("left")

        time.sleep(2)
        keyboard.press_and_release('ctrl+w')

        counter = counter - 1
        if counter == 0:
            ender = False
            playsound('assets/sound/alert.mp3')  # Plays a sound when aborting
            break


if __name__ == '__main__':
    downloader()