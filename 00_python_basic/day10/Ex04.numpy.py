import numpy as np

# 난수 발생 : 하나의 프로그램에서 여러사람이 난수를 발생하면, 그때마다 다른 값이 나온다.
#               이렇게 다른 값이 나오는 것을 방지하기 위해서 seed 를 사용한다.
# np.random.seed(인수=정수=시작값지정)
np.random.seed(0)

# 난수 5개 생성
print(np.random.rand(5))

# 이제 seed 0 의 난수는 이걸로 고정된다.

print("ㅡ" * 30)

# 데이터 섞기 : shuffle
x = np.arange(10)
print(x)

np.random.shuffle(x)
print(x)





