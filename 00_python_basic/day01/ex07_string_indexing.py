# 인덱싱 indexing : 원하는 위치를 지정
# 슬라이싱 slicing : 잘라내기

# 인덱싱 => 0 부터 시작하고, 왼쪽에서 오른쪽 
#           (음수인 경우는 -1 부터 시작하고, 오른쪽에서 왼쪽으로)
#   [위치값] 

str = "Hello Python"
print(str[6]) # P

print(str[-1]) # n
print(str[-5]) # y

print('ㅡ' * 30)

# 슬라이싱 : 원하는 위치에서 원하는 갯수 만큼만 추출
#   [시작위치 : 끝위치(포함안됨)]          
#   끝위치 - 시작위치 = 갯수

print(str[6:8] , type(str[6:8])) # Py
print(str[8:6] , type(str[8:6])) # 안나옴
# 작은수 에서 큰수 로 가야한다.
print(str[-3:-5] , type(str[-3:-5])) # 안나옴
print(str[-5:-3] , type(str[-5:-3])) # yt

print('ㅡ' * 30)

# Hello 추출하기 
print(str[0:5])
# (처음부터 중간까지)
print(str[:5])

# Python 추출하기 (중간부터 끝까지)
print(str[6:])

# 전체 (처음부터 끝까지)
print(str)
print(str[:])

print('ㅡ' * 30)

# 틀린 글자 변경하기

# ** 가변형 자료형 : 리스트 list , 딕셔너리 dict , 집합 set => 추가, 삭제, 수정 가능

# ** 불변형 자료형 : 문자열 str , 튜플 tuple => 수정 불가능 

str = "pithon"
#str[1] = 'y' 
# 불변형 자료이므로 오류 발생

#        p              thon
str2 = str[:1] + 'y' + str[2:]
print(str2)



