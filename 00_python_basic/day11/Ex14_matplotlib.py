import matplotlib.pyplot as plt
import numpy as np

# 한글 깨짐 처리 
plt.rcParams["font.family"]="Malgun Gothic"
# False로 설정하면 Matplotlib이 마이너스 기호에 표준 ASCII 하이픈-마이너스 (-)를 사용
plt.rcParams['axes.unicode_minus'] =False
plt.rcParams["font.size"]= 10

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1,1,1)

# 평균0, 표준편차 1표준 정규분포
x = np.random.randn(1000)

# 히스토그램  (bins =10 이면 10개 구간)
ax.hist(x, bins=100)

ax.set(title="histogram", xlabel="x axis", ylabel="y axis")

plt.show()



