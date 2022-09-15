# 자동화를 하다보면 파일을 다루는 경우가 많음
# 파일 기본 배우기

import os

'''
◆ 경로 관련 내용
1. 경로 확인 및 변경
os.getcwd() : 현재 디렉토리 확인 
    --> get current workspace directory
os.chdir(상대경로 또는 절대경로) : 경로변경
    - os.chdir(하위폴더) : 하위폴더로 이동
    - os.chdir("..") : 부모 폴더
    - os.chdir("../..") : 조부 폴더
    - os.chdir("C:/") : 절대경로 이동

2. 경로생성
os.path.join : 경로 합치기
os.path.join(os.getcwd(),"my_file.txt") : 현재경로 + my_file --> 새로운 경로

3. 경로에서 폴더정보 가져오기
    - 파일경로에서 폴더 정보가져옴
    - r"경로" : 경로를 문자그대로 인지함 (역슬래쉬를 탈출문자로 인지안하게됨)
'''

# # 1. 경로 확인 및 변경
# print(os.getcwd())
# os.chdir("2_desktop") # 하위 폴더중 2_desktop으로 이동
# os.chdir("..") 
# os.chdir("../..") 
# os.chdir("C:/") 

# # 2. 경로생성
# print(os.getcwd())
# print(os.path.join(os.getcwd(),"my_file.txt")) # 절대경로 생성

# # 3. 경로에서 폴더정보 가져오기
# print(os.path.dirname(r"C:\Users\chang\CCWWORKSPACE\Inflearn\nadocoding\RPA\my_file.txt"))
# print("-"*50)

'''
◆파일 정보 관련
1. 생성날짜 / 수정날짜 / 마지막 접근 날짜
    - os.path.getctime(경로)
    - os.path.getmtime(경로)
    - os.path.getatime(경로)

날짜 형식으로 변환
    - datetime.datetime.fromtimestamp(변수)
    - datetime.datetime.fromtimestamp(변수).strftime("%Y-%m-%d %H:%M:%S")
    
2. 파일 사이즈
    - os.path.getsize(경로)
'''

# 파일 정보 가져오기
import time
import datetime 

# file_path = "screenshot.png"
# ctime = os.path.getctime(file_path)
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y-%m-%d %H:%M:%S"))

# mtime = os.path.getmtime(file_path)
# print(mtime)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S"))

# atime = os.path.getatime(file_path)
# print(atime)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y-%m-%d %H:%M:%S"))

# # 파일 크기 --> 바이트단위
# fsize = os.path.getsize(file_path)
# print(fsize)

