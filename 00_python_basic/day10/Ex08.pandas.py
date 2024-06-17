# pandas 
# 시리즈 : 1차원벡터 데이터에 행방향 인덱스를 붙인 것
# 데이터프레임 : 2차원 행렬 데이터에 인덱스를 붙인 것

import pandas as pd
from pandas import DataFrame

# 데이터 프레임 생성

# 1. 하나의 열이 되는 데이터를 리스트나 1차원 배열로 준비

# 2. 각각의 열에 대한 이름을 key 로 가지고 있는 딕셔너리 만들기

# 3. 데이터를 DataFrame 생성자에 넣기

# 4. 열 방향 인덱스는 colums 인수를 사용하고, 행 방향 인덱스는 index 인수로 지정

# 1.
df = DataFrame(["뽀로로", "패디", "크롱", "루피", "에디"])
print(df)

print("ㅡ" * 30)

# 2.
df2 = DataFrame({
    "name" : ["뽀로로", "패티", "크롱", "루피", "에디"]
})
print(df2) # 위에 name 표시

print("ㅡ" * 30)

# 3.
df3 = DataFrame({
    "name" : ["뽀로로", "패티", "크롱", "루피", "에디"] ,
    "id" : ["pororo", "paty", "cron", "rupy", "edi"]
})
print(df3)

print("ㅡ" * 30)

# 4.
df4 = DataFrame({
    "name" : ["뽀로로", "패티", "크롱", "루피", "에디"] ,
    "id" : ["pororo", "paty", "cron", "rupy", "edi"]
}, index=["no_1", "no_2", "no_3", "no_4", "no_5"])
print(df4)

print("ㅡ" * 30)

# 데이터 프레임 생성2
data = {
        "2015": [9904312, 3448737, 2890451, 2466052],
        "2010": [9631482, 3393191, 2632035, 2431774],
        "2005": [9762546, 3512547, 2517680, 2456016],
        "2000": [9853972, 3655437, 2466338, 2473990],
        "지역": ["수도권", "경상권", "수도권", "경상권"],
        "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]}
#print(data, type(data)) # 딕셔너리

columns = ["지역", "2015", "2010", "2005", "2000", "2010-2015 증가율"]
index = ["서울", "부산", "인천", "대구"]
df5 = DataFrame(data, index=index, columns=columns)
print(df5)

print("ㅡ" * 30)

df5.index.name = "도시별"
df5.columns.name = "년도별"
print(df5)


print("ㅡ" * 30)















