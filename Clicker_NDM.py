import time
import mouse
import keyboard
import pyautogui
import emoji
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

        time.sleep(2)

        # Click Here Btn
        mouse.move(x=1216, y=830)
        mouse.click("left")

        time.sleep(2)

        # Download Btn
        mouse.move(x=955, y=915)
        mouse.click("left")

        time.sleep(3)

        # MINIMIZE NDM DOWNLOAD BAR
        mouse.move(x=1140, y=237)
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
            break


if __name__ == '__main__':
    downloader()