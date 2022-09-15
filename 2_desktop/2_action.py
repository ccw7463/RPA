import py
import pyautogui
import time

# ◆ 클릭 관련 ◆
'''
1. FILE TAB 위치 좌표 확인 
    - pyautogui.sleep(2)
    - pyautogui.position()
2. Click 하기
    - pyautogui.click() --> 현재 마우스 위치를 클릭(마우스눌렀다뗐다)
    - pyautogui.click(x좌표,y좌표) --> 해당 좌표 위치를 클릭
    - pyautogui.click(clicks = 500) --> 500번 클릭
3. 또다른 Click 방법
    - pyautogui.mouseDown() --> 마우스 클릭
    - pyautogui.mouseUp() --> 마우스 떼기
    - pyautogui.click() = mouseDown + mouseUp
4. 추가 클릭
    - pyautogui.doubleClick() --> 더블 클릭
    - pyautogui.rightClick() --> 마우스 우클릭
    - pyautogui.middelClick() --> 휠 클릭
5. 드래그 앤 드롭
    - 방법1 : Down -> 이동 -> Up
    - 방법2 : pyautogui.drag 사용
        - 절대좌표 이동 --> pyautogui.dragTo(x이동,y이동,duration)
        - 상대좌표 이동 --> pyautogui.drag(x이동,y이동,duration)
        - duration을 설정안해주면 안되는거같네? 
6. 스크롤 
    - pyautogui.scroll(300) --> 양수(위) / 음수(아래)
'''
# 커서 위치 정보 확인
pyautogui.sleep(1)
print(pyautogui.position())

# vs code FILE TAB 클릭
pyautogui.click(1320,25,duration=1)

# 파일 드래그 앤 드롭
pyautogui.moveTo(194,1119,duration=1)
pyautogui.mouseDown()
pyautogui.moveTo(285,827,duration=1)
pyautogui.mouseUp()

pyautogui.drag(100,0,duration=1)
pyautogui.dragTo(620,816,duration=1)

# 스크롤
pyautogui.moveTo(2485,521,duration=1)
pyautogui.scroll(500)