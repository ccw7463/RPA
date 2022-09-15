import pyautogui

'''
추가기능
1. 마우스 커서 위치와 RGB 값 정보를 알려주는 프로그램
    - pyautogui.mouseInfo()
2. 자동화 멈추기
    - 마우스 커서를 네개 모퉁이중 아무곳에나 두면 된다.
    - 해당 기능 방지 --> pyautogui.FAILSAFR = False (추천기능은아님)
3. 모든 동작에 sleep 적용
    - pyautogui.PAUSE = 시간
'''

# pyautogui.mouseInfo()  

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False
for i in range(6):
    pyautogui.move(100,100)
    