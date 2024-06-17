import numpy as np

# zero : 크기가 정해진 모든 값이 0 인 배열 생성
z_ar = np.zeros(5)
print(z_ar, type(z_ar), z_ar.dtype) # float64 => 실수 64비트

print("ㅡ" * 30)

# 2차원 배열
z_ar2 = np.zeros((2, 3))
print(z_ar2)

print("ㅡ" * 30)

# 크기를 지정하지 않고, 다른 배열의 크기를 참고해서 만든다.
# 값은 1로 들어간다.
one_ar = np.ones_like(z_ar)
print(one_ar)

print("ㅡ" * 30)

# 즉, 원본과 동일한 크기로 만들면서, 값은 1로 초기화
one_ar2 = np.ones_like(z_ar2)
print(one_ar2)

print("ㅡ" * 30)

arr = np.arange(10) # range 와 같은 개념
print(arr) # [0 1 2 3 4 5 6 7 8 9]

print("ㅡ" * 30)

# arange(시작, 끝, 간격)
arr2 = np.arange(3, 21, 2) # 3 부터 21 미만 , 간격은 2씩
print(arr2) 

print("ㅡ" * 30)

# linspace(시작, 끝, 개수) => 균등분할(끝포함 됨!)
ls = np.linspace(0, 100, 2) # [  0. 100.]
print(ls)
ls = np.linspace(0, 100, 5) # [  0.  25.  50.  75. 100.]
print(ls)

# 끝포함 하지 않고 싶으면 => endpoint=False
ls = np.linspace(0, 100, 2, endpoint=False) # [ 0. 50.]
print(ls)
ls = np.linspace(0, 100, 5, endpoint=False) # [ 0. 20. 40. 60. 80.]
print(ls)

print("ㅡ" * 30)







