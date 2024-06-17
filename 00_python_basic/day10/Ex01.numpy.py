import numpy as np

# 1차원 배열을 다차원배열로 변경할 때 reshape 함수 사용
# (단, 전체 크기, 개수는 변경되지 않는다.)

ar = np.arange(12) # 0 ~ 11
print(ar, len(ar)) # 개수 : 12

print("ㅡ" * 30)

bar = ar.reshape(3, 4)
print(bar, len(bar)) # 행의 개수 : 3 (2차원배열의 경우 행의 개수가 나온다.)
print(len(bar[0])) # 열의 개수 : 4 => 총 개수 : 3 * 4 = 12

print("ㅡ" * 30)

bar2 = ar.reshape(2, 2, 3)
print(bar2, len(bar2)) # 면의 개수 : 2 (3차원배열의 경우 면의 개수가 나온다.)
print(len(bar2[0]), len(bar2[0][0])) # 행의 개수 : 2, 열의 개수 : 3
#                                   => 총개수 : 2 * 2 * 3 = 12

print("ㅡ" * 30)

bar3 = ar.reshape(3, -1) # (3, 4) 와 같다.
print(bar3, len(bar3)) # 3행이면서 전체 개수에 맞춰서 열을 맞춰준다.
# -1 경우 => 전체 개수와 첫번째 값을 가지고 계산에 의해서 결정된다.

print("ㅡ" * 30)

# 다차원배열을 1차원배열로 변경 : flatten 함수 사용 
bar4 = np.arange(12).reshape(3, 4)
print(bar4) # 3행 4열 행렬
print(bar4.flatten()) # 다시 [ 0  1  2  3  4  5  6  7  8  9 10 11]
# 같은 결과 ravel()
print(bar4.ravel())

print("ㅡ" * 30)

bar5 = np.arange(12).reshape(2, 3, 2)
print(bar5) # 2면 3행 2열 행렬
print(bar5.flatten()) # 다시 [ 0  1  2  3  4  5  6  7  8  9 10 11]
# 같은 결과 ravel()
print(bar5.ravel())

print("ㅡ" * 30)

# flatten 함수와 ravel 함수의 차이점
ori_arr = np.array([[1, 2, 3], [4, 5, 6]])
f_arr = ori_arr.flatten()
r_arr = ori_arr.ravel()

# 차이를 보기 위해서 원본을 변경하자
ori_arr[0, 0] = 100 # 맨처음
ori_arr[-1, -1] = 500 # 맨끝
print(ori_arr)
print(f_arr) # [1 2 3 4 5 6]
print(r_arr) # [100   2   3   4   5 500]


# flatten : 원본이 변경되어도 변경되지 않는다.(원본을 복사해서 사용)
# ravel : 원본이 변경되면 같이 변경된다.(원본을 그대로 사용)

print("ㅡ" * 30)


