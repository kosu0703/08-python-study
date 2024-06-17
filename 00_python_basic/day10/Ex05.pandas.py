# 시계열 데이터(시리즈 = Series = numpy의 1차원) 
# or
# 데이터 프레임(DataFram = table = numpy의 2차원 = 행렬)

import pandas as pd

# 시리즈 생성
# 2017년도 도시별 인구 데이터
city = pd.Series([9857426, 1502227, 2475231, 3470653])
print(city) # 1차원을 표형태로 나타낸다.

print("ㅡ" * 30)

# index = 인덱스 레이블(라벨)
city2 = pd.Series([9857426, 1502227, 2475231, 3470653], 
                 index=['서울', '대전', '대구', '부산'])
print(city2, type(city2)) # pandas.core.series.Series

print("ㅡ" * 30)

print(city2.index)  # 인덱스 출력
print(city2.values) # 값 출력

print("ㅡ" * 30)

city2.name = "2017년 도시별 인구수"
print(city2)



print("ㅡ" * 30)






