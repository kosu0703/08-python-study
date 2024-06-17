# 람다식 : 보통 함수를 간결하게 만들 때 사용한다.

# 사용방법
#   함수이름 = lambda 매개변수1 , 매개변수2 , ... : 매개변수를 활용한 표현식

# ** return 예약어가 없어도 표현식의 결과값을 반환한다.

# 매개변수는 생략가능
str = lambda : "Hello"
# 함수이기 때문에 함수명 뒤에 () 괄호를 붙여줘야한다
print(str())

# 람다식 함수
str2 = lambda a, b : a + b
res = str2(7, 3)
print(res)

# 일반 함수
def str3(a, b) :
    return a + b
res = str3(7, 3)
print(res)









