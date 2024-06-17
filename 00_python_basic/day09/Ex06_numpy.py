# 전치 연산 : 행과 열을 교환
#            T 속성 사용함 => 2차원배열변수.T

# 2차원 배열의 행과 열을 바꿀때 사용 
# ex) 2행 3열.T => 3행 2열

import numpy as np

ar = np.array([[1, 2, 3], [4, 5, 6]])
print(ar)
print(ar.shape) # (2, 3)

print("ㅡ" * 30)

print(ar.T)
print(ar.T.shape) # (3, 2)

print("ㅡ" * 30)
