import pandas as pd

city = pd.Series([9857426, 1502227, 2475231, 3470653], 
                 index=['서울', '대전', '대구', '부산'])

div = city / 1000000
print(div) # 각 요소마다 나눈다.

print("ㅡ" * 30)

# 시리즈 인덱싱
print(city[1], city["대전"])
print(city[3], city["부산"])

print("ㅡ" * 30)

# 여러개
print(city[[1, 3, 0]])
print(city[['대전', '부산', '서울']])

print("ㅡ" * 30)

# 슬라이싱
print(city[1:3])            # 인덱스는 마지막을 포함 하지 않는다.
print(city['대전':'부산'])  # "부산"은 포함된다. 

print("ㅡ" * 30)

x = pd.Series(range(3), index=["a", "b", "다"])
print(x)

print(x.a)
print(x.b)
print(x.다) # 한글이여도 값이 가져와진다.






print("ㅡ" * 30)