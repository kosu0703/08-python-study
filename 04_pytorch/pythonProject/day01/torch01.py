# 파이토치 설치
# facebook 에서 개발
# 오픈 소스 딥러닝 라이브러리
# 강력한 GPU 가속화를 통한 Tensor 계산
# 설치 : 터미널에서 conda install pytorch torchvision torchaudio -c pytorch 명령어 실행
#       또는 파일에서 pip install torch

import torch
import numpy as np

# a.shape : 모양 확인
# a.dim() : 차원 확인
# a.size() : 크기 확인
# a[:5], a[3:] : 슬라이싱 가능
a = torch.tensor(np.arange(10)) # numpy 를 통한 생성
b = torch.FloatTensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) # tensor 자체 생성

print(a.shape, b.shape)
print(a.size(), b.size())
print("-" * 100)

print(a.dim(), b.dim())
print("-" * 100)

# 슬라이싱
print(a[:5]) # 0 ~ 4
print(a[3:]) # 3 ~ 9
print("-" * 100)

# torch.FloatTensor
#   - pytorch 에서 사용되는 데이터 타입 중 하나
#   - 실수로 이루어진 텐서를 의미
#   - 다차원 배열로, Numpy 의 배열과 유사

# cf) 다차원 배열 : 1차원(벡터), 2차원(행렬), 3차원(텐서)

# 1차원 텐서 생성
tensor1d = torch.FloatTensor([1.0, 2.0, 3.0])
print(tensor1d, tensor1d.shape, tensor1d.size())

# 2차원 텐서 생성
tensor2d = torch.FloatTensor([[1.0, 2.0], [3.0, 4.0]])
print(tensor2d, tensor2d.shape, tensor2d.size())

# 3차원 텐서 생성
tensor3d = torch.FloatTensor([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]])
print(tensor3d, tensor3d.shape, tensor3d.size())
print("-" * 100)

a = torch.FloatTensor([1, 1])
b = torch.FloatTensor([6, 6])
print(a + b) # tensor([7, 7]) => index 에 맞춰서 연산이 이루어짐

a = torch.FloatTensor([1, 10])
b = torch.FloatTensor([6])
print(a + b) # tensor([7, 16]) => 벡터의 모든 index 에 스칼라를 더함

# a = 1 * 2 , b = 2 * 1
# 브로드 캐스팅 : 작은 텐서의 크기를 자동으로 큰 텐서의 크기와 맞추는 것
a = torch.FloatTensor([[1, 7]])
b = torch.FloatTensor([[5], [6]])

# a = [[1, 7], [1, 7]]
# b = [[5, 5], [6, 6]]

# [[1, 7],   +   [[5, 5],    =   [[1+5, 7+5],
#  [1, 7]]        [6, 6]]         [1+6, 7+6]]

print(a + b) # tensor([[ 6., 12.], [ 7., 13.]])
print("-" * 100)

# 행렬 곱셈
a = torch.FloatTensor([[1, 2], [3, 4]])
b = torch.FloatTensor([[1], [2]])

# a 의 첫번째 행과 b 의 첫번째 열
# 1 * 1 + 2 * 2 = 5
# 3 * 1 + 4 * 2 = 11

print(a.matmul(b)) # tensor([[ 5.], [11.]])
print("-" * 100)

# 그냥 곱셈
a = torch.FloatTensor([[1, 2], [3, 4]])
b = torch.FloatTensor([[1], [2]])
# 브로드 캐스팅 후 같은 위치에 있는 것 끼리 계산
# a = [[1, 2], [3, 4]]
# b = [[1, 1], [2, 2]]
# a * b = [[1*1, 2*1], [3*2, 4*2]]
print(a * b) # tensor([[1., 2.],  [6., 8.]])
print("-" * 100)
# 위와 같다
print(a.mul(b)) # tensor([[1., 2.],  [6.,8.]])

