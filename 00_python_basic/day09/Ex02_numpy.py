# numpy 는 ndarray 클래스를 사용한다. (다차원배열 = N차원 배열)

import numpy as np

# 2차원 배열 : 1차원 배열 여러개를 하나로 묶은 것
#       - 행과 열로 구성된 행렬(matrix 매트릭스 형태)
#       - 단, 1차원 배열의 길이가 같아야 한다.

# [[...], [...], [...]] : 리스트 안에 리스트 

two_ar = np.array([[0, 1, 2], [3, 4, 5]]) # 2행 3열
#two_ar = np.array([[0, 1, 2], [3, 4, 5, 6, 7]]) # 배열의 길이가 다르면 오류

print(two_ar, type(two_ar), two_ar.shape) # (2, 3)

print(two_ar * 3) # 모든 요소 3배

print("ㅡ" * 30)

print("행의 갯수 : ", len(two_ar))
print("열의 갯수 : ", len(two_ar[0])) # 배열안에 배열의 길이가 모두 같기 때문에

print("ㅡ" * 30)

# 2차원 배열의 각 값에 접근하기 : 배열변수[행 index][열 index]
for i in range(0, len(two_ar)) :
    for j in range(0, len(two_ar[i])) : # 각 행의 열의 갯수 만큼 돌자
        print('two_ar[{0}][{1}] : {2}' .format(i, j, two_ar[i][j]))

print("ㅡ" * 30)

# 3차원 배열 만들기
# : 값의 종류가 같고, 행과 열 개수가 동일한 2차원 배열들의 묶음

# 행, 열, 면
three_ar = np.array([   # 3행 4열
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] ,             # 0면
    [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]   # 1면 
    ])

print(three_ar.shape) # (2, 3, 4) => 2면 3행 4열

print("depth : ", len(three_ar))        # 면의 개수
print("row : ", len(three_ar[0]))       # 행의 개수
print("column : ", len(three_ar[0][0])) # 열의 개수

print("ㅡ" * 50)

# 3차원 배열의 각 값에 접근하기 : 배열변수[면 index][행 index][열 index]
for i in range(len(three_ar)) :
    for j in range(len(three_ar[i])) :
        for k in range(len(three_ar[i][j])) :
            print('three_ar[{}][{}][{}] : {}' .format(i, j, k, three_ar[i][j][k]), end="  ")
        print()
    print("ㅡ" * 50)

# range 에 0 안써도 , {} 안에 번호 안써도 가능하다. 

print("ㅡ" * 30)

# 크기가 다른 두 행렬의 연산 지원
a1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
a2 = [1, 2, 3]

b1 = np.array(a1)
b2 = np.array(a2)

print(b1 + b2) # 각 행에 더해진다.
print(b1 * b2) # 각 행에 곱해진다.

print("ㅡ" * 30)

# 배열의 차원(ndim)과 크기(shape) 알아내기
c1 = np.array([1,2,3,4,5])
c2 = np.array([[0, 1, 2], [3, 4, 5]])
c3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] ,            
                [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]])

# 1차원 배열
print(c1.ndim)  # 1
print(c1.shape) # (5,)
# 2차원 배열
print(c2.ndim)  # 2
print(c2.shape) # (2, 3)
# 3차원 배열
print(c3.ndim)  # 3
print(c3.shape) # (2, 3, 4)



print("ㅡ" * 30)