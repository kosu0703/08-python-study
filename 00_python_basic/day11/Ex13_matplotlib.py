import matplotlib.pyplot as plt
import numpy as np

# 한글 깨짐 처리 
plt.rcParams["font.family"]="Malgun Gothic"
# False로 설정하면 Matplotlib이 마이너스 기호에 표준 ASCII 하이픈-마이너스 (-)를 사용
plt.rcParams['axes.unicode_minus'] =False
plt.rcParams["font.size"]= 10

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)

x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6, 15, 7]


ax.scatter(x,y, label="x")
ax.scatter(x2,y2, label="x2")

ax.set(title="scatter plot", xlabel="x axis", ylabel="y axis")

plt.show()



