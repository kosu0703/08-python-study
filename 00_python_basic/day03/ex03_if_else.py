# 항목 in 리스트, 튜플, 문자열 => 항목이 존재하면 true
# 항목 not in 리스트, 튜플, 문자열 => 항목이 존재하지 않으면 true

# data(값) in 리스트
print(1 in [1, 2, 3, 4, 5]) # True
print(10 in [1, 2, 3, 4, 5]) # False

print("ㅡ" * 30)

print(1 not in [1, 2, 3, 4, 5]) # False
print(10 not in [1, 2, 3, 4, 5]) # True

print("ㅡ" * 30)

pocket = ['phone', 'money', 'paper']

if 'money' in pocket :
    print("택시 타고 가라")
else :
    print("걸어가")
    
print("ㅡ" * 30)

# pass 
# 조건식의 참, 거짓에 따라 실행할 행동을 정의하는게 아니라
# 아무런 일도 하지 않도록 설정하고 싶을 때 => pass

# 주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 걸어가라
if 'money' in pocket :
    pass
else :
    print("걸어가")

print("안녕히가세요")

print("ㅡ" * 30)

# 조건부 표현식 : 변수 = 참인 경우 if 조건식 else 거짓인 경우

str = "택시 타고 가라" if 'money' in pocket else "걸어가라"

print(str) # 택시 타고 가라

str = "택시 타고 가라" if 'card' in pocket else "걸어가라"

print(str) # 걸어가라

print("ㅡ" * 30)




