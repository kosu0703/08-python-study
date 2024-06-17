# 집합 : 중복을 허용하지 않는다. 순서가 없다.
#       인덱싱으로 값을 얻을 수 없다.

s1 = set([1, 2, 3, 4, 5])
print(s1, type(s1)) # {1, 2, 3, 4, 5} , set

# 리스트 - [] 대괄호
# 튜플 - () 괄호
# 딕셔너리 - { key : valu } 중괄호
# 집합 - {} 중괄호 
s2 = {100, 200, 300, 400, 500}
print(s2 , type(s2))

# 중복불가
s3 = set([1, 2, 3, 4, 5, 1, 5, 7, 5, 2, 10, 9])
print(s3 , type(s3))

# 인덱싱으로 값을 얻을 수 없다.
#print(s3[4]) # 오류발생

# 리스트나 튜플로 형변환해서 인덱싱 사용
s3_list = list(s3)
print(s3_list[4])

s3_tuple = tuple(s3)
print(s3_tuple[4])

print("ㅡ" * 30)

# 교집합(&), 합집합(|), 차집합(-) 가능
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# 교집합
print(s1&s2)

# 합집합
print(s1|s2)

# 차집합 => 앞에 있는 것 기준
print(s1-s2)
print(s2-s1)

print("ㅡ" * 30)

# 추가, 삭제, 전체 삭제
#s3 = s1 + s2 # 오류 발생

# 추가 => add 또는 update
s1.add(10) # 한개씩 추가
print(s1)

s1.update(s2) # 여러개 추가
print(s1)

print("ㅡ" * 30)

# 삭제 => remove(data(값)) 
s1.remove(10)
print(s1)

# 인덱싱으로 값을 얻을 수 없기 때문에
# del 사용 불가능
#del s1[2]

# 없는 요소 삭제 시 오류발생
#s1.remove(100) 

# discard() => 삭제하고자 하는 요소가 없어도 오류 발생 안함
s1.discard(100)
print(s1)

print("ㅡ" * 30)

# in 을 사용해서 데이터 존재여부 검사 가능
# data(값) in 집합
print(100 in s1) # False
print(1 in s1) # True

print("ㅡ" * 30)

# 전체 삭제 => clear
s1.clear()
print(s1) # set()

print("ㅡ" * 30)

