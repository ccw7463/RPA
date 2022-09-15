import pyautogui
import time
import sys


def find_target(img_file,timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if (end-start) >= timeout:
            print("시간 종료")
            break
    return target

def my_click(img_file,timeout=30):
    target = find_target(img_file,timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s Target not found ({img_file}) Terminate program")
        sys.exit()

img_file = "notepad.png"
timeout = 5
my_click(img_file,timeout)