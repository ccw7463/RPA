from openpyxl import Workbook
excel = Workbook()
ws = excel.active

# 이미지 삽입
from openpyxl.drawing.image import Image

img = Image("img.png") # --> 300 x 300 이미지
ws.add_image(img,"C3") 

excel.save("image.xlsx")
excel.close()

