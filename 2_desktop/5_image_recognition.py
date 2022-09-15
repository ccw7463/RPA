'''
pyautogui를 가지고 윈도우 자동화를 할때는 
자동화대상이 되는 영역을 이미지로 만들고, 그 이미지를 
전체 또는 지정된 화면에서 찾는 방식으로 동작함
'''

import pyautogui

# file_menu.png 저장한걸 불러와서 해당 위치 찾기 --> 저장 : Win + Shift + s
file_menu = pyautogui.locateOnScreen("file_menu.png")
print(file_menu)

pyautogui.click(file_menu,duration=1)

# 똑같은게 두개이상일때는? --> pyautogui.locateAllOnScreen
'''
for i in pyautogui.locateAllOnScreen("checkbox.png"):
    print(i)
    pyautogui.click(i,duration=0.25)
'''

# 속도개선
'''
1. GrayScale
    trash_icon = pyautogui.locateOnScreen("trash_icon.png",grayscale=True)
    pyautoguo.moveTo(trash_icon)
        --> 속도30%향상, 정확도하향
2. 범위 지정
    trash_icon = pyautogui.locateonScreen("trash_icon.png,region=(x,y,width,height))
    pyautoguo.moveTo(trash_icon)
        --> 검색범위를 지정하는 방법
3. 정확도 조정
    --> 이미지가 어느정도 같으면 맞다고 하는것
    --> pip install opencv-python 
    --> 기존 confidence = 0.999 임
    trash_icon = pyautogui.locateOnScreen("trash_icon.png,confidence=0.5)
'''

# 대기 --> 자동화하려는 대상이 뜰때까지 대기
'''
1. 계속 기다리기 --> while문을 통해 구현
'''
file_menu_notepad = pyautogui.locateOnScreen("notepad.png")

while file_menu_notepad is None:
    file_menu_notepad = pyautogui.locateOnScreen("notepad.png")
    print("발견 실패")

pyautogui.click(file_menu_notepad)

'''
2. 일정 시간동안 기다리기 --> TimeOut
'''
import time
import sys

timeout= 10 # 10초 대기
start = time.time() # 시작 시간 설정
file_menu_notepad = None
while file_menu_notepad is None:
    file_menu_notepad = pyautogui.locateOnScreen("notepad.png")
    end = time.time()  # 종료 시간 설정
    if (end-start) >= timeout:
        print("시간 종료")
        sys.exit()

pyautogui.click(file_menu_notepad)


