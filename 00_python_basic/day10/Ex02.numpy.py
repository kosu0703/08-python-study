import numpy as np

# 벡터의 내적 : 두 벡터의 차원이 같아야 한다.
#           - 각 요소의 곱을 모두 더한 것이다.
#           - dot 함수 사용 => 결과는 스칼라(값)로 나온다.

a = np.array([2, 5, 1])
print(a, type(a)) # numpy.ndarray => 다차원배열(N-Dimension-Array)

b = np.array([4, 3, 5])
print(b, type(b))

# 내적 구하기
print(np.dot(a, b.T)) # (2 * 4) + (5 * 3) + (1 * 5) = 28

print("ㅡ" * 30)

# matrix 행렬 곱셈 => matmul 함수 사용
c = np.array([[2, 1], [1, 4]])
d = np.array([[1, 2, 0], [0, 1, 2]])
print(np.matmul(c, d)) # [[2, 5, 2], [1, 6, 8]]






print("ㅡ" * 30)


