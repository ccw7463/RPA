import pyautogui

#  스크린샷 기능
img = pyautogui.screenshot() # 현재 화면 스크린샷하여 파일로 저장
img.save("screenshot.png")

# 주어진 커서좌표에서 한개의 픽셀값을 가져옴
'''
pyautogui.pixel(x좌표,y좌표,(R,G,B)) --> True / False 값 리턴
'''
pixel = pyautogui.pixel(1279,20)
print(pixel)

print(pyautogui.pixelMatchesColor(1279,20,(38,121,177)))
print(pyautogui.pixelMatchesColor(1279,20,(38,110,177)))