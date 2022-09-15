# 파일 복사하기

# 어떤파일을 폴더안으로 복사하기

import os
import shutil

if os.path.exists("test_folder"):
    pass
else:
    os.mkdir("test_folder")

'''
파일 복사하기
@ : "경로" + "파일이름" 

복사방법 
1. shutil.copy(@,@) --> 원본경로, 대상경로/파일/대상경로+파일 모두 가능
2. shutil.copyfile(@,@) --> 원본경로, 파일만 가능
3. shutil.copy2(@,@)

- copy, copyfile : 메타정보 복사 X
- copy2 : 메타정보 복사 O
- 이미 동일이름을 가진 파일이있으면 복사안됨
'''
# 원본경로, 대상경로/파일/대상경로+파일 모두 가능
shutil.copy("file_menu.png","test_folder") 
shutil.copy("file_menu.png","test_folder/copied_file_menu.png")

# 원본경로, 파일만 가능
shutil.copyfile("file_menu.png","test_folder/copied_file_menu2.png")

# copy, copyfile : 메타정보 복사 X
# copy2 : 메타 정보 복사 O
shutil.copy("file_menu.png","test_folder/copy.png")
shutil.copy2("file_menu.png","test_folder/copy2.png")

# 폴더 복사
shutil.copytree("test_folder","test_folder2")

# 폴더 이동
shutil.move("test_folder2","test_folder")