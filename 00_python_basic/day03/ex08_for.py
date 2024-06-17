# for 변수 in 리스트 :  ( 튜플, 문자열, 집합, 딕셔너리 도 가능 )
#       수행할 문장1
#       수행할 문장2
#       수행할 문장3

# 리스트
t_list = ["one", "two", "three"]

for i in t_list :
    print(i)
    
print("ㅡ" * 30)

# 튜플
t_tuple = ("red", "green", "blue")

for k in t_tuple :
    print(k)

print("ㅡ" * 30)

# 문자열
t_str = "hello"

for i in t_str :
    print(i)

print("ㅡ" * 30)

# 집합 - 순서없이 무작위, 중복불가
t_set = {"하나", "둘", "셋"}

for k in t_set :
    print(k)

print("ㅡ" * 30)

# 딕셔너리
t_dic = {
    "name" : "hong" ,
    "phone" : "010-7777-9999" ,
    "addr" : "서울" ,
    "age" : 24
}

for k in t_dic.keys() :
    print(k , ":" , t_dic[k])

print("ㅡ" * 30)

# 리스트 안에 튜플
t_list = [(1, 2), (3, 4), (5, 6)]

for (i, j) in t_list :
    print(i + j)

print("ㅡ" * 30)

# 딕셔너리에서 key : value 를 둘다 뽑아내자
for k, v in t_dic.items() :
    print(k , ":" , v)


print("ㅡ" * 30)