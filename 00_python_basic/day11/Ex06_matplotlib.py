# https://matplotlib.org/ 사이트 참조

import matplotlib.pyplot as plt

# (3,3) => 가로와 세로의 크기를 나타내고, 단위 인치이다.
# fig = plt.figure(figsize=(3,3))
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# plt.show()

# 창 분할
fig = plt.figure()
# 1행 2열의 첫번째
# ax1 = fig.add_subplot(1,2,1)
# 1행 2열의 두번째
#ax2 = fig.add_subplot(1,2,2)

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()
