import torch
import numpy as np

# Numpy 에서 Reshape, pytorch 에서는 View

a = np.arange(24)
print(a)
print('-' * 100)

# 2행 4열
# -1 : 자동으로 배치한다.
a = a.reshape(-1, 2, 4)
print(a)
print('-' * 100)

# 3차원 2행 4열
print(a.shape) # (3, 2, 4)
print('-' * 100)

# 파이토치에서는 뷰를 사용해라
b = torch.FloatTensor(np.arange(24))
print(b)
print('-' * 100)

print(b.view([-1, 4]))
print('-' * 100)

print(b.view([-1, 2, 4]))
print('-' * 100)

