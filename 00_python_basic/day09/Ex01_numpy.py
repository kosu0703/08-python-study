# numpy 모듈 : 대규모, 다차원 배열을 다루기 위한 모듈
#               - 기본적으로 array 라는 자료형을 사용한다.(행렬의 개념과 비슷함)
#               - 아나콘다 설치시 함께 설치된다.(따로 설치 : pip install numpy)
#               - import numpy as np 호출
#               - 리스트 자료형과 아주 유사함 (인덱싱과 슬라이싱)

import numpy as np

# 1차원 배열 다루기 : numpy array([한가지 종류가 저장된 리스트])
#                   리스트를 배열로 바꿔서 사용함

# 배열변수 = np.array([list])
#   - 배열변수 : 할당된 배열공간의 주소를 참조하는 레퍼런스 변수임(주소저장변수)
#   - 배열로 만들 리스트는 반드시 정수 or 실수 값들로만 구성되어 있어야 한다.

'''
    리스트 : - , / 연산 불가능 
            + 연결 , * 반복연산
            
    배열 : + , - , * , / 모두 가능
    
'''





# 정수
ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ar, type(ar))    
# numpy.ndarray 는 다차원 배열 구조 => 선형대수 계산에 이용

# 실수
ar2 = np.array([1.1 , 2.2, 3.3, 4.4, 5.5])
print(ar2, type(ar2))

# 정수 + 실수 => 실수
ar3 = np.array([1, 2, 3.14, 4, 5.23, 6, 7.777])
print(ar3, type(ar3))

# str
ar4 = np.array(['aaa', 'bbb', 'ccc', 'ddd', 'eee'])
print(ar4, type(ar4))

# str + 숫자 => str
ar5 = np.array(['aaa', 2, 'ccc', 4.3, 'eee']) 
print(ar5, type(ar5))

# 자료형을 하나로 통일 시킨다.
# 머신러닝에서는 정수 or 실수만 있고, str 은 없다.

print("ㅡ" * 30)

# 스칼라 : 크기만을 가진 값 , ex) a = 24
# 벡터 : 크기와 방향을 모두 가진 값 , ex) 배열(numpy 의 array)

# 리스트일때 벡터화(배열) 연산 처리의 예
datalist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 리스트 각 요소를 2배로 증가하자
for i in datalist :
    datalist[i] = i * 2
    
print(datalist) 
# 보통 원본은 건들지 않고 빈거를 만들어서 넣는다.
# 원본은 훼손되면 안되기 때문에

print("ㅡ" * 30)

datalist2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 리스트를 배열로 만들어서 각 요소를 2배로 증가하자
ar = np.array(datalist2)
print(ar * 2) # [ 0  2  4  6  8 10 12 14 16 18]

# 리스트를 벡터처럼 사용하면 리스트가 두배로 늘어난다.
print(datalist2 * 2) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("ㅡ" * 30)

a = [1, 2, 3, 4, 5]
b = np.array(a)

# 리스트와 배열 연산의 차이
print(a + a) # 반복 => [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(b + b) # 계산 => [ 2  4  6  8 10]

print("ㅡ" * 30)

print(a * 2) # 반복
print(b * 2) # 계산

print("ㅡ" * 30)

# 배열은 비교연산, 논리연산, 산술연산이 가능하다.
ar1 = np.array([1, 2, 3])
br1 = np.array([10, 20, 30])

print(2 * ar1 + br1) # [12 24 36]
# 2 * ar1[0] + br1[0] = 12

print(br1 == 2) # [False False False]
print(ar1 == 2) # [False True False]
print(ar1 >= 2) # [False True True]
print((ar1 == 2) & (br1 > 10)) # [False  True False] 
# ar1[0] == 2 (F) & br1[0] > 10 (F) => False

print("ㅡ" * 30)




