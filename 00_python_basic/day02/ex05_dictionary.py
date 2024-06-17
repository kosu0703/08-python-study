# 딕셔너리 => key , value 로 이루어져 있음
#           { key1 : value1 , key2 : value2 , ... }
dic = {
    'name' : 'hong',
    'phone' : '010-7777-9999',
    'age' : 24,
    'gender' : True
    }
print(dic , type(dic))

# cf) value 에는 리스트가 들어갈 수 있다.

print("ㅡ" * 30)

# 추가
dic = {
    1 : 'a' ,
    "2" : "b"
}
print(dic , type(dic))

# key : value 에서는 index 가 없다.
# 그냥 key 는 name 일 뿐이다.
dic[5] = 'c'
dic[4] = 'k'
print(dic , type(dic))

print("ㅡ" * 30)

# 리스트 추가
dic[3] = [1, 2, 3, 4]
print(dic , type(dic))

# 튜플 추가
dic[6] = (1, 2, 3, 4)
print(dic , type(dic))

# 딕셔너리 추가
dic[10] = {
    'name' : 'kim',
    'phone' : '010-1234-5678',
    'age' : 33
}
print(dic , type(dic))

print("ㅡ" * 30)

# 삭제 => del 딕셔너리[key]
del dic[6]
print(dic , type(dic))

del dic[10]['phone']
print(dic , type(dic))

print("ㅡ" * 30)

# 수정 => key 가 같으면 덮어쓰기 된다.
dic[5] = 'K'
print(dic , type(dic))

dic[10]['name'] = 'go'
print(dic , type(dic))

print("ㅡ" * 30)

# 딕셔너리 관련 함수
dic = {
    'name' : 'hong',
    'phone' : '010-7777-9999',
    'age' : 24,
    'gender' : True
}

# 키 값 불러오기 => keys()
print(dic.keys() , type(dic.keys())) # dict_keys

# 데이터 값 불러오기 => values()
print(dic.values() , type(dic.values())) # dict_values

# key , value 같이 불러오기 => items()
print(dic.items() , type(dic.items())) # dict_items

print("ㅡ" * 30)

# 리스트가 필요한 경우
print(list(dic.keys()) , list(dic.values()))
# 리스트로 변경하면 append, insert, pop, remove, sort 등을 사용할 수 있다.

print("ㅡ" * 30)

# key : value 모두 지우기 => clear
dic.clear()
print(dic , type(dic)) # {} , dict

print("ㅡ" * 30)

dic = {
    'name' : 'hong',
    'phone' : '010-7777-9999',
    'age' : 24,
    'gender' : True
}

# 얻기 => get(key) 또는 딕셔너리[key]
print(dic.get('name'))
print(dic['name'])

# 없는 key 를 호출했을 때
print(dic.get('addr')) # None
#print(dic['addr']) # 오류발생
# 되도록 get 을 사용하자

# key 가 없으면 None 이 아니라 'movie' 가 나온다. => default 값 지정가능
print(dic.get('hobby', 'movie')) 

print("ㅡ" * 30)

# key 값 조사하기 => in
print('name' in dic) # True
print('email' in dic) # False

print("ㅡ" * 30)










