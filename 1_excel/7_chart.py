from openpyxl import load_workbook
excel = load_workbook("sample.xlsx")
ws = excel["score"]

# 차트 만들기
from openpyxl.chart import BarChart, Reference, LineChart

# B2:D11 까지의 데이터를 Bar 차트로 생성
bar_data = Reference(ws,min_row=2,max_row=11,min_col=2,max_col=4) # 어떤 데이터를 chart로 만들지에 대해 정의
bar_chart = BarChart() # 차트 종류 설정(Bar, Line, Pie,..)
bar_chart.add_data(bar_data) #데이터 추가
ws.add_chart(bar_chart,"F3") # 차트 넣을 위치 정의 

# B2:D11 까지의 데이터를 Line 차트로 생성
line_data= Reference(ws,min_row=1,max_row=11,min_col=2,max_col=4)
line_chart = LineChart()
line_chart.add_data(line_data, titles_from_data=True) # --> 첫번째 행을 legend로 사용
line_chart.title = "성적표" # --> 차트 제목
line_chart.style = 10 # --> 미리 정의된 스타일 적용 (사용자가 개별 지정도 가능)
line_chart.y_axis.title = "점수" # --> y축 제목 설정
line_chart.x_axis.title = "과목" # --> x축 제목 설정
 
ws.add_chart(line_chart,"F16")
excel.save("sample.xlsx")
