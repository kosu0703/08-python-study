# def 함수명(매개변수) :
#       수행할 문장1
#       수행할 문장2
#       수행할 문장3
#       [return 데이터]

def add(a, b) :
    return a + b

def sub(a, b) :
    print(a - b)

# 함수 호출
# 리턴이 있을 때
res = add(10, 5)
print(res)
# 리턴이 없을 때
sub(7, 3)

# 같은 함수명이 여러개 존재할 수 없다.(오버로딩이 안됨)
# 이름이 같은 함수를 다시 선언하면 위에 함수가 없어진다.(덮어쓰기 됨)
def sub(a) :
    print(10 - a)

sub(3) # 오류 안남
#sub(4, 10) # 오류 발생

print("ㅡ" * 30)

# 받는 매개변수의 값을 모를 때 => *args 사용
def add_many(*args) :
    print(args)

add_many(1, 2, 3)
add_many(2, 4, 6, 8, 10, 12)

print("ㅡ" * 30)

# * 을 붙이면 전부 모아 튜플로 만들어 준다.
def add_mul(choice, *args) :
    if choice == 'add' :
        result = 0
        for i in args :
            result += i
    elif choice == 'mul' :
        result = 1
        for i in args :
            result *= i
    else :
        result = "add 또는 mul 중에 선택해주세요."
    return result        

res = add_mul("add", 1, 2, 3, 4, 5)
print(res)

res = add_mul("mul", 1, 2, 3, 4, 5, 6, 7)
print(res)

res = add_mul("sub", 1, 2, 3, 4, 5)
print(res)

print("ㅡ" * 30)

