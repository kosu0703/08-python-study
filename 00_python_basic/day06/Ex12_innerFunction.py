# 파이썬의 내장 함수는 외부 모듈과 달리 import 가 필요없다.
# 바로 사용 가능

# abs() : 절대값
print(abs(3))
print(abs(-3))
print(abs(3.2))
print(abs(-3.2))

print("ㅡ" * 30)

# all([리스트]) : 반복 가능한 자료형(리스트)을 입력받아
#               해당 요소가 모두 참이면 결과는 참, 하나라도 거짓이면 거짓
#               ( and 와 같은 개념 )
print(all([True, True, True, True])) # True
print(all([True, False, True, True])) # False

print(all([1, 2, 3, 4, 8, 9])) # Trun ( 0 이외의 숫자는 True )
print(all([1, 2, 3, 0, 8, 9])) # False ( 0 이면 False )

print(all(['apple', 'banana', '    '])) # True ( 문자가 있으면 True ) , 공백문자 포함
print(all(['apple', '', 'mango'])) # False ( '' 문자가 없으면 False )

print("ㅡ" * 30)

# any([리스트]) : 반복 가능한 자료형(리스트)를 입력 인수로 받아
#               해당 요소가 모두 거짓이면 결과는 거짓, 하나라도 참이면 참
#               ( or 와 같은 개념 )
print(any([True, True, True, True])) # True
print(any([True, False, True, True])) # True
print(any([1, 2, 3, 4, 8, 9])) # Trun 
print(any([1, 2, 3, 0, 8, 9])) # True 
print(any(['apple', 'banana'])) # True 
print(any(['apple', '', 'mango'])) # True 
print(any([''])) # False

print("ㅡ" * 30)

# chr(i) : 유니코드 숫자를 받아서 그 코드에 해당하는 문자를 리턴하는 함수
print(chr(97))      # a
print(chr(44032))   # 가

print("ㅡ" * 30)

# ord("문자") : 해당 문자의 유니코드 숫자를 리턴하는 함수
print(ord('a'))     # 97
print(ord('가'))    # 44032

print("ㅡ" * 30)

# 몫 따로 나머지 따로
print(7//3 , (7%3))
print(type(7//3), type(7%3)) # 자료형 int

# divmod(a, b) : 몫과 나머지를 튜플 형태로 반환
print(divmod(7,3), type(divmod(7,3))) # 자료형 튜플

print("ㅡ" * 30)

# ** enumerate : 순서가 있는 데이터를 입력받아서 인덱스값을 포함하는 enumerate 객체 리턴
#               (리스트, 튜플, 문자열)                          (차례대로 접근하는 객체)

#       - 보통 for 문과 같이 사용한다.
#       - 데이터 값을 이용해서 인덱스 값을 추출할 때 유용하다. 

for i, name in enumerate(['body', 'food', 'bar']) :
    print(i, name)
    
print("ㅡ" * 30)

# eval("문자열") : 실행 가능한 문자열을 입력받아 문자열을 실행한 결과를 돌려주는 함수
print(1 + 2)    # 3
print("1 + 2")  # 1 + 2

print(eval("1 + 2"))  # 3

print("ㅡ" * 30)

print(divmod(7,3))          # (2, 1)
print(eval("divmod(7,3)"))  # (2, 1)

print("ㅡ" * 30)

# ** filter(함수, 반복 가능한 데이터) : 반복 가능한 데이터의 요소 순서대로 함수를 호출했을 때 
#                                   리턴값이 참인 것만 묶어서 리턴한다.

def positive(lis) : # 리스트를 받아서 
    result = []     # 결과를 저장하는 리스트
    for i in lis :
        if i > 0 :  # 0 보다 큰 자료만 리스트에 별도로 저장
            result.append(i)
    return result
print(positive([1, 2, -1, 5, -4, 0, 9])) # [1, 2, 5, 9]
# 필터 사용
print(list(filter(lambda x : x > 0 , [1, 2, -1, 5, -4, 0, 9])))

# 짝수만
print(list(filter(lambda x : x % 2 == 0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    
print("ㅡ" * 30)
    
# int(x) : 문자열 형태의 정수나 실수를 정수로 리턴
print("3" , type("3"))          # str
print(int("3"), type(int("3"))) # int

print("3.53" , type("3.53"))        # 3.53 str
print(int(3.53), type(int(3.53)))   # 3 int

# float(x) : 문자열 형태의 실수를 실수로 리턴
print(float("3.53"), type(float("3.53")))   # 3.53 float
    
print("ㅡ" * 30)

# list("문자열") : 문자열을 리스트로 변경 => 문자열을 문자의 배열로 생각하기 때문에
#                       한 글자씩 리스트로 만듦
print(list("python")) # ['p', 'y', 't', 'h', 'o', 'n']

print("ㅡ" * 30)

# len() : 반복가능한 자료형의 길이 (리스트, 튜플, 문자열)
print(len("python"))            # 6
print(len([1,2,3,4,5,6,7]))     # 7
print(len((1,2,3,4,5,6,7,8)))   # 8

print("ㅡ" * 30)

# ** map(함수, 반복 가능한 데이터) 

# 가지고 있는 리스트 요소 두배 만들기
def two_times(lis) :
    result = []
    for i in lis :
        result.append(i*2)
    return result
print(two_times([1, 2, 3, 4, 5])) # [2, 4, 6, 8, 10]

# map 사용
def two_times2(x) :
    return x * 2
print(list(map(two_times2, [1, 2, 3, 4, 5])))

# 받은 요소를 가지고 무언가를 하면 map
# 받은 요소에서 몇개를 걸러내면 filter

print("ㅡ" * 30)

# max : 반복 가능한 자료형을 받아서 최대값을 리턴
# min : 반복 가능한 자료형을 받아서 최소값을 리턴
print(max([2, 3, 1, 5, 7, 4, 8, 3, 9, 2])) # 9
print(min([2, 3, 1, 5, 7, 4, 8, 3, 9, 2])) # 1

print(max("pythonPYTHON"))  # y (소문자가 대문자보다 크다)
print(min("pythonPYTHON"))  # H (유니코드 숫자)

print("ㅡ" * 30)

# ** range([start, ] stop, [step]) : for 문과 자주 사용하는 함수
#                                       끝포함 안함
print(list(range(10, 20, 2))) # [10, 12, 14, 16, 18]
# stop 만 있으면 0 부터 시작
print(list(range(5))) # [0, 1, 2, 3, 4]

print("ㅡ" * 30)

# round : 반올림
print(round(4.2)) # 4
print(round(4.5)) # 4
print(round(4.6)) # 5
print(round(5.5)) # 6

print("ㅡ" * 30)

# sorted : 입력 데이터를 정렬한 후 리스트로 리턴한다. (단, 원본은 그대로)
print(sorted([3, 1, 2]))    # [1, 2, 3]
print(sorted('zero'))       # ['e', 'o', 'r', 'z']

print("ㅡ" * 30)

# sum : 입력 데이터 합계
print(sum([1, 2, 3])) # 6
print(sum((1, 2, 3))) # 6

print("ㅡ" * 30)

# tuple : 튜플로 만들기
print(tuple('abc'))     # ('a', 'b', 'c')
print(tuple([1, 2, 3])) # (1, 2, 3)

print("ㅡ" * 30)

# str : 문자열로 만들기
print(str(3) , type(str(3)))
print(str(3.42) , type(str(3.42)))

print("ㅡ" * 30)

















