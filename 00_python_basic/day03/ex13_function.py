# 매개변수에 초기값을 미리 지정할 수 있다.

def say(name, age, gender = True) :
    print("나의 이름은 {} 입니다." .format(name))
    print("나의 나이는 {} 입니다." .format(age))
    if gender :
        print("나의 성별은 남성 입니다.")
    else :
        print("나의 성별은 여성 입니다.")
        
say("hong", 25, True)

print("ㅡ" * 30)

say("kim", 21, False)

print("ㅡ" * 30)

say("ko", 32)
  
print("ㅡ" * 30)

# 초기값 지정해준 뒤에 변수를 적으면 오류발생
#def say(name, gender = True , age) :

# 매개변수에 초기값을 미리 저정할 때, 
# 반드시 뒤에는 없거나 초기값이 지정되는 매개변수가 있어야 한다.
def say(name, gender = True , age = 24) :
    print()
    
# 초기값이 있으면 맨 뒤로 빼자




