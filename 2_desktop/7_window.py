import py
import pyautogui

# forground window

fw = pyautogui.getActiveWindow() # 현재 활성화된 창
print(fw.title) # 창의 제목 정보
print(fw.size) # 창의 크기 정보 (가로,세로)
print(fw.left,fw.top,fw.right,fw.bottom)  # 창의 좌표 정보


# pyautogui.click(fw.left+25,fw.top+20)

# 모든 윈도우 가져오기
for w in pyautogui.getAllWindows():
    print(w) 

# 어떤 제목을 가지는 윈도우 가져오기
w = pyautogui.getWindowsWithTitle("계산기")[0]

'''
윈도우 다루기
    - 활성화 : w.activate() --> 활성화확인 : w.isActive
    - 최대화 : w.maximize() --> 최대화확인 : w.isMaximized
    - 최소화 : w.minimize() --> 최소화확인 : w.isMinimized
    - 되돌리기 : w.restore()
    - 닫기 : w.close()
'''
# 활성화 (맨 앞으로 가져오기) --> 최대/최소/원복기능
if w.isActive == False:
    w.activate()
pyautogui.sleep(2)
if w.isMaximized == False:
    w.maximize()
pyautogui.sleep(2)

# if w.isMinimized == False:
#     w.Minimize()

w.restore()
pyautogui.sleep(2)

w.close() 