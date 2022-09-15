import pyautogui


# 다음영상 재생직전 정지상태라면 녹화시작
stop_button = pyautogui.locateOnScreen("stop_button.png")
if stop_button:
    x = stop_button[0]
    y = stop_button[1]
    print("재생시작")
    video_start = pyautogui.locateOnScreen("video_click.png")
    x = video_start[0] + 37
    y = video_start[1] + 6
    pyautogui.moveTo(x,y)
    pyautogui.click(duration=0.2)
    pyautogui.moveTo(x-100,y)
else:
    pass


# 재생중인지 확인
video_state = pyautogui.locateOnScreen("video_state.png")

if video_state:
    print("정지중입니다.")
    print(video_state)
    x = video_state[0]
    y = video_state[1]
    pyautogui.moveTo(x,y)
else:
    print("재생중입니다.") 
    print(video_state) # 재생중이면 None 값 리턴
    pass





