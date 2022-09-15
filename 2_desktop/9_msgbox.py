import pyautogui

print("곧 시작합니다..")
pyautogui.countdown(2)  # 3초동안 카운트다운해줌 --> 터미널창에 나타남 


'''
pyautogui.alert(메시지,제목) : 확인 버튼만 있는 팝업
pyautogui.confirm(메시지,제목,예/아니요) : 예/아니요 선택 가능 팝업
pyautogui.prompt(메시지,입력) : 입력받는 파업
pyautogui.password(메시지) : 암호입력하는 팝업
'''
print("자동화 시작")

pyautogui.alert("자동화 수행 실패하였습니다.", "경고") # 확인 버튼만 있는 팝업

pyautogui.confirm("계속 진행하시겠습니까?","확인",("예썰","아니용"))

result1 = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?","입력") # 사용자 입력
print(result1)

result2 = pyautogui.password("비밀번호를 입력하세요.") # 암호 입력
print(result2)