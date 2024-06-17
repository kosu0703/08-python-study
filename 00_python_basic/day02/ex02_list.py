# list : 대괄호 사이에 쉼표로 구분된 값(항목)의 목록 
#       (다른 언어의 배열과 비슷하다.)
#   ** 자바와 다르게 서로 다른 유형의 항목들을 포함할 수 있다.
#   리스트는 가변형이다.
odd = [1, 3, 5, 7]
str = ["hi", "bye", "good"]
person = ["홍길동", 24, 180.1, 'A', True]

# 리스트도 인덱싱과 슬라이싱이 가능하다.

# 인덱싱을 하면 끄집어낸 자료의 자료형이지만,
print(odd[2] , type(odd[2])) # 5 , int
# 리스트를 슬라이싱을 하면 리스트로 나온다.
print(odd[0:2] , type(odd[0:2])) # [1, 3] , list
# 음수이면 오른쪽부터
print(str[-1] , type(str[-1])) # good , str

print("ㅡ" * 30)

# 리스트 안에 리스트가 존재할 수 있다.
even = [2, 4, 6, odd, 8, 10]
print(even)
print(even[0] , type(even[0]))
print(even[3] , type(even[3]))  # 리스트가 나오고, 자료형도 리스트이다.
print(even[3][2]) # 5  

# 문자열도 가능하다 
print(person[0][1]) # 길
# ** str 을 list 로 보고있다.







