# 리스트 연산

# 리스트 더하기 ( + )
su1 = [1, 2, 3]
su2 = [4, 5, "홍길동", 6, 7]
res = su1 + su2
print(res) # [1, 2, 3, 4, 5, '홍길동', 6, 7]

# 리스트 반복하기 ( * )
res = su1 * 3
print(res) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

#res = su1[1] + "hi" # 오류발생
#print(res) # int 와 str 을 더할 수 없다

# int 를 str 로 형변환 해야한다.
# 형변환 : 자료형(대상) => int(), float(), str(), list(), ...
res = str(su1[1]) + "hi"
print(res)

print("ㅡ" * 30)

# 리스트 항목 추가, 삭제, 수정 가능 (가변형이기 때문에)
odd = [1, 7, 5, 3, 9]

# 항목 추가 => append(항목) => 맨뒤에 들어간다.
odd.append(11)
print(odd)

# 항목 수정 => 리스트[index] = data(값)
odd[2] = 13
print(odd)

# 항목 삭제 => del 리스트[index] 또는 remove(data(값))
del odd[2]
print(odd)

odd.remove(7)
print(odd)

# 항목 삽입 => insert(index, data(값))
odd.insert(2, 13)
print(odd)

# 리스트 정렬 => sort()
odd.sort()
print(odd)

# 문자열도 정렬 가능 (아스키코드표 순서대로)
# 숫자 > 대문자 > 소문자 > 한글
str = ['a', 'c', 'A', '한', 'e', 'b', '1', 'B', 't']
str.sort()
print(str)

# 리스트 뒤집기 => reverse
str = ['a', 'c', 'A', '한', 'e', 'b', '1', 'B', 't']
str.reverse()
print(str)

print("ㅡ" * 30)

# 리스트 요소 끄집어 내기 

# pop => 맨 끝에 있는 항목 삭제하기
odd = [1, 2, 3, 4, 5]
res = odd.pop() # 삭제하기 전에 저장할 수 있다.
print(odd , res)

print("ㅡ" * 30)

# 리스트 확장 => extend(리스트)
su1 = [1, 2, 3, 4, 5] 
su1.extend([7, 8, 9])
print(su1)
# 중복 가능
su1.extend([1, 3, 5, 7])
print(su1)






print("ㅡ" * 30)