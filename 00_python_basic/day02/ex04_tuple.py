# 튜플 : 몇가지를 제외하고 리스트와 거의 같음
#       - 불변형이므로 수정이 안된다.
#       - 괄호 사용 ( 항목 , 항목 , 항목 )

# 튜플 생성
t1 = (1, 2, 3)
print(t1 , type(t1)) # (1, 2, 3) , tuple

# 빈 튜플 생성
t2 = ()
print(t2 , type(t2)) # () , tuple

# 하나의 데이터만 들어있는 튜플 => 튜플이 아니다.
t3 = (3) 
print(t3 , type(t3)) # 3 , int 

# 요소가 하나만 있을경우 튜플로 만들고 싶다면
# 반드시 요소 뒤에 , 콤마를 붙여야 한다.
t4 = (4, )
print(t4 , type(t4)) # (4, ) , tuple

# data(값)이 여러개 일때는 () 생략 가능
t5 = 1, 2, 3, 4, 5
print(t5 , type(t5))

print("ㅡ" * 30)

# 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0] , type(t1[0]))

# 슬라이싱
print(t1[1:] , type(t1[1:]))

print("ㅡ" * 30)

# 더하기 ( + )
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t1 = t1 + t2
print(t1) # 튜플은 불변형인데 변경이 된다

# 곱하기 ( * ) => 반복
print(t2 * 3)

# 길이 구하기 ( len )
print(len(t1))

print("ㅡ" * 30)

# 튜플 항목 삭제, 수정 안됨
t1 = (1, 2, 'a', 'b')

# 삭제 del => 오류발생
#del t1[1]
#print(t1)

# 수정 => 오류발생
#t1[2] = 'A'
#print(t1) 

t1 = (1, 2, 'a', 'b')
# 튜플은 변경이 불가능해서 많이 사용되진 않는다.
# 하지만 변경 못하게 막아야하는 상수 같은 경우에 사용한다.

# 튜플의 항목을 삭제, 수정하려면
# 튜플을 리스트로 형변환하고 삭제, 수정 하자
t1_list = list(t1)
print(t1_list , type(t1_list))

del t1_list[2]
print(t1_list)

t1_list[2] = 'B'
print(t1_list)

t1 = tuple(t1_list)
print(t1)

print("ㅡ" * 30)