# 판다스 설치 : pip install pandas

import pandas as pd

# 엑셀 파일 읽기
data = pd.read_excel("day05/data/excel02.xlsx")

# 상위 데이터 확인 (5개)
print(data.head())

print("ㅡ" * 30)

# 하위 데이터 확인 (5개)
print(data.tail())

print("ㅡ" * 30)

# 전체 데이터 확인
print(data)

print("ㅡ" * 30)

# 전체 행과 열의 갯수
print(data.shape) # (20, 7) => 행이 20개, 열이 7개

print("ㅡ" * 30)

# csv 파일로 만들기
data.to_csv('day05/data/excel_csv.csv')
# 인덱스 번호 사용 안함
data.to_csv('day05/data/excel_csv2.csv', index=False)

print("ㅡ" * 30)


