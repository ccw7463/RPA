# 데스크탑 자동화시작
'''
윈도우에서 제공하는 object 정보를 사용하는게아니라, 이미지 기반으로 진행
1. 설치 : pyautogui
'''

# 사이즈확인
import pyautogui
size = pyautogui.size() # 현재화면의 스크린 사이즈 가져옴
print(size) # size[0] : width / size[1] :height 

# ◆ 마우스 이동 ◆
'''
모니터화면 맨 왼쪽위 = (0,0)
1. 절대좌표로 이동 --> pyautogui.moveTo(x좌표,y좌표)
2. 상대좌표로 이동 --> pyautogui.move(x이동값,y이동값)
    - 현재커서가 있는 위치로부터 이동임.

마우스 위치 좌표 확인 --> pyautogui.position()
    - 해당 메소드는 인덱싱 가능
    - 예) pyautogui.position()[0] : x좌표 리턴
'''

# 1. 절대좌표로 이동
pyautogui.moveTo(50,50) # 지정한 위치로 마우스를 이동
print(pyautogui.position())
pyautogui.moveTo(200,200,duration=0.25) # 1초동안 해당 위치로 이동
print(pyautogui.position())
pyautogui.moveTo(400,400,duration=0.25)
print(pyautogui.position())

# 2. 상대좌표로 이동
pyautogui.move(300,300,duration=0.25)
print(pyautogui.position())
pyautogui.move(300,300,duration=0.25)
print(pyautogui.position())
