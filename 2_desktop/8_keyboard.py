import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

'''
pyautogui.write(내용)
내용에 들어가는 것
    1. 숫자 또는 영어 (기존은 한글지원X)
        - 한글 지원 필요사항 : pip install pyperclip
    2. 리스트 --> 명령어를 넣을 수 있음.
        - 'left', 'right', 'enter' 등등
        - 관련내용 : automate the boring stuff with python 검색
            - ch20 --> 검색 : keyboard attribute 
            - 여기서 필요한 key 확인가능
    3. 특수문자
        - pyautogui.keyDown("shift")
        - pyautogui.press("4")
        - pyautogui.keyUp("shift")
            --> shift 키 누른상태에서 4를 입력하고 shift 키 뗀다.
            --> $ 표시 가능
'''
# 숫자 또는 영어
pyautogui.write("123132")
pyautogui.write("nadocoding", interval=0.1)
pyautogui.write("나도코딩") # 한글은 안됨...나중에설명해준다하심

# 한글 지원하기
import pyperclip
pyperclip.copy("나도코딩") # --> 나도코딩 글자를 클립보드에 저장
pyautogui.hotkey("ctrl","v") # 클립보드에 있는 내용을 붙여넣기

# 한글 지원 함수로 구현하기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")
my_write("코딩코딩")

# [] 리스트 형태로 작성시, 한 단어를 넣을순 없는거같다. 기능 또는 단어하나만 입력가능
pyautogui.write(["t","e","s","t","left","left","right","right","enter"],interval=0.2)
pyautogui.write("next")

'''
특수문자 및 조합키
    - pyautogui.keyDown(값) : 값 누르기
    - pyautogui.keyUp(값) : 값 떼기

    - pyautogui.hotkey("ctrl","alt","shift","a")
        - ctrl 누르고 > alt 누르고 > shift 누르고 > a 누르고 > a 떼고 > shift 떼고 > alt 떼고 > ctrl 떼기
'''
# 특수문자
pyautogui.keyDown("shift")
pyautogui.press("4")
pyautogui.keyUp("shift")

# 조합키 (복붙)
pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.keyDown("c")
pyautogui.keyUp("c")
pyautogui.keyUp("ctrl")

pyautogui.write(["right"])
pyautogui.keyDown("ctrl")
pyautogui.keyDown("v")
pyautogui.keyUp("v")

# 조합키 (Hot key 사용)
pyautogui.hotkey("ctrl","a")

# 자동화 프로그램 종료
'''
윈도우 : ctrl + alt + del
맥 : cmd + shift + option + q
'''

