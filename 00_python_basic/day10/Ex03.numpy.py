import numpy as np

# 브로드캐스팅
# 벡터(행렬)끼리 덧셈 또는 뺄셈을 하려면, 행과 열의 개수가 같아야 함(원칙)
# numpy 에서는 행과 열이 다른 벡터 끼리도 연산이 가능하도록 지원
# 이 기능을 브로드캐스팅이라고 한다.

# 크기가 작은 벡터가 자동으로 크기가 큰 벡터의 행과 열 개수와 맞춰진다.(확장)

x = np.arange(5)
y = np.ones_like(x)

print(x + y)
print(x + 5)

print("ㅡ" * 30)

# 배열 연결 : 두개이상의 배열들을 연결해서 하나의 큰 배열을 만듦
# hstack, vstack, dstack , stack

# hstack(horizental stack) : 행의 개수가 같은 2차원배열을 좌우로 합칠때 사용 
#                           => 열의 개수가 늘어남
ar1 = np.ones((2, 3))
ar2 = np.zeros((2, 2))
print(np.hstack([ar1, ar2]))

print("ㅡ" * 30)

# vstack(vertical stack) : 열의 개수가 같은 2차원 배열들을 위아래로 합칠때 사용
#                           => 행의 개수가 늘어남
ar3 = np.ones((2, 3))
ar4 = np.zeros((3, 3))
print(np.vstack([ar3, ar4]))

print("ㅡ" * 30)

# dstack(depth stack) : 배열의 깊이 방향으로 결합하는 함수로, 
#                       기본적으로 axis=2 로 한 stack 과 같다.

# 2차원 이하의 배열은 3차원으로 확장된 후에 결합된다. (m, n) -> (m, n, 1)
ar5 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(ar5)
ar6 = np.array([[5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
print(ar6)
ar7 = np.dstack([ar5, ar6])
print(ar7, ar7.shape) # (3면 4행 2열)

print("ㅡ" * 30)

# stack : 2차원 배열 여러개를 깊이(depth) 방향으로 합칠때 사용
#         => a행 b열 배열의 개수가 n개 합쳐지면, 결과는 n면 a행 b열 이 된다.
ar8 = np.stack([ar5, ar6], axis=2)
print(ar8)

print("ㅡ" * 30)
