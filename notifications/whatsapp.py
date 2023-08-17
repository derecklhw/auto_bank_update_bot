import pywhatkit as kit
import pyautogui
from pynput.keyboard import Key, Controller
   
import time

keyboard = Controller()

def send_message(msg):
    try:
        kit.sendwhatmsg_instantly(
            phone_no="+23057647563", 
            message=msg,
            tab_close=True
        )
        time.sleep(10)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(e)
        return