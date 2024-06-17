# 파이썬의 자료형 : 숫자(int, float), 문자열(str), 논리형(bool), 
#               **리스트, 튜플, 딕셔너리, 집합 => 변경이 가능한 것과 불가능한 것이 있다.

# boolean : 참/거짓 => 조건식에 많이 사용한다. (분석할 때도 반복문과 조건식이 제일 많이 나온다.)

# 참 : True , 거짓 : False (**주의 : 첫글자 대문자)
con = True
print(con)
print(type(con))

# 변수는 하나의 정보만 가진다.
con = False
print(con)
print(type(con))

con = 'Hello~'
print(con)
print(type(con))

# 문자열 10개 출력
print('*' * 10)

# 숫자를 boolean 형으로 변경하자 : bool(숫자)
# 0 이면 False , 0 을 제외한 숫자는 True 로 만든다.
su1 = 0
su2 = 1
su3 = 135
print(bool(su1))
print(bool(su2))
print(bool(su3))

# 문자열을 boolean 형으로 변경하자 : bool(문자열)
# 데이터가 있으면 True , 데이터가 없으면 False
str1 = 'hi'
str2 = ''
str3 = ' '  
print(bool(str1))
print(bool(str2))
print(bool(str3))
# 띄어쓰기도 공백문자이므로 True

# 나머지 자료형도 같다. => 비어있으면 False , 데이터가 있으면 True



