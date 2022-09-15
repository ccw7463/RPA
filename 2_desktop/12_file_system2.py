import os

'''
@: "경로" + "파일이름" 

◆ 파일 목록 관련
os.listdir(경로) : 경로 파일 가져오기
os.walk(경로) : 하위폴더 내용 모두 포함

만약 경로가 현재경로라면? --> (".") 로 설정

경로가 파일인지 폴더인지?
    - 파일인가? : os.path.isfile(@)
    - 폴더인가? : os.path.isdir(@)

주어진 경로가 존재하는지?
    - os.path.exists(경로)

파일 관련
    - 파일명 변경 : os.rename(@,@)
    - 파일 삭제 : os.remove(@)

폴더 관련
    - 폴더 만들기 : os.mkdir(@)
        - 하위폴더를 가지는 폴더만들기 : os.makedirs("new_folders/a/b/c")
    - 폴더명 변경 : os.rename(@,@)
    - 폴더 지우기 : os.rmdir(@) --> 폴더안이 비었을때만 삭제 가능
    - 폴더 지우기(2) : shutil.rmtree("new_folders") --> 폴더안이 비어있지않아도 삭제가능
        - 주의해서 사용해야함!
'''

# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir(os.getcwd()+"/1_excel")) # 주어진 폴더 밑에서 모든폴터, 파일목록 가져오기


# 파일 목록가져오기 (하위 폴더 내용 모~두 포함)
result = os.walk(r"C:\Users\chang\CCWWORKSPACE\Inflearn\nadocoding\RPA")

for root,dirs,files in result:
    print(root,dirs,files)
    print("-"*60)


# 만약 폴더내에서 특정 파일들을 찾으려면?
name = "11_file_system.py"
result = []

for root,dirs,files in os.walk(r"C:\Users\chang\CCWWORKSPACE\Inflearn\nadocoding\RPA"):
    if name in files:
        result.append(os.path.join(root,name))
print(result)


# 특정 패턴을 가지는 파일을 찾으려면?
# *.xlsx, *.txt, 자동화*.png 등등...
import fnmatch
pattern  =  "*.py" # .py로 끝나는 모든 파일
result = []
for root, dirs, files in os.walk("."):
    for name in files:
        if fnmatch.fnmatch(name,pattern):   # name과 pattern 이 일치하면
            result.append(os.path.join(root,name))
print(result)

# 주어진 경로가 파일인지? 폴더인지?
print(os.path.isdir(".")) # --> 경로인지?
print(os.path.isfile(".")) # --> 폴더인지?

# 주어진 경로가 존재하는지?
if os.path.exists("1_excel"):
    print("파일 또는 폴더가 존재합니다.")
else:
    print("존재하지 않습니다.")

# 파일명 변경하기 
os.rename("file_menu2.png","file_menu.png")

# 파일 삭제하기
os.remove("file_menu2 copy.png")

# 하위폴더가지는 폴더생성
os.makedirs("new_folder/a/b/c")

# 폴더명 변경하기
os.rename("new_folder","new_folder2")

# 폴더 지우기
os.rmdir("new_folder2")

# # 폴더 지우기 2 --> 비어있지않아도 삭제가능
# import shutil
# shutil.rmtree("new_folder2")
