# 리스트 컴프리헨션 : [ 표현식 for 항목 in 리스트 ]

# 끄집어 내서, 앞으로 가서, 계산 후 리스트에 담는다.
result = [ i * 10 for i in range(2, 10) ]
print(result , type(result))

# 조건을 줄 수 있다.
# [ 표현식 for 항목 in 리스트 if 조건식 ]
result = [ i * 3 for i in range(1, 11) if i % 2 == 1]
print(result , type(result))

# 결과는 리스트이다.



