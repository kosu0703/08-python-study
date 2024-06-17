import pandas as pd

# 리스트 객체에서 시리즈 생성
city = pd.Series([9857426, 1502227, 2475231, 3470653], 
                 index=['서울', '대전', '대구', '부산'])

# in : 주로 검색 용도로 사용
print("서울" in city) # True
print("수원" in city) # False

print("ㅡ" * 30)

for k, v in city.items() :
    print("{} : {}" .format(k, v))

print("ㅡ" * 30)

# 딕셔너리 객체에서 시리즈 생성
dic = {"서울" : 1002218, "대전" : 151875, "대구" : 248782, "부산" : 351377}
city2 = pd.Series(dic)
print(city2)

print("ㅡ" * 30)

# 인덱스 기반의 연산
res = city - city2
print(res) # 시리즈

res2 = city.values - city2.values
print(res2) # 리스트

print("ㅡ" * 30)

# 딕셔너리는 순서가 없다 
dic2 = {"서울" : 1002218, "대전" : 151875, "대구" : 248782, "부산" : 351377, "인천" : 292581}
city3 = pd.Series(dic2)
res3 = city - city3 # NaN = Not a Number
print(res3)
print(res3.notnull()) # 데이터가 없으면 False

print("ㅡ" * 30)

print(res3[res3.notnull()]) # 데이터가 없으면 출력하지 말아라

print("ㅡ" * 30)

# 인덱스 기반의 연산 데이터 
city2["부산"] = 777153
print(city2) # 있으면 변경

city2["광주"] = 845153
print(city2) # 없으면 생성

del city2["서울"] 
print(city2) # 삭제


print("ㅡ" * 30)







