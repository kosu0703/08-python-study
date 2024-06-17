import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.set_xlim([0., 10.]) # x축, 0-10까지 표현
ax1.set_ylim([-0.5, 2.5]) # x축, 0-10까지 표현
ax1.set_title("matplot sample", size=15)
ax1.set_xlabel('x_axis', size=10)
ax1.set_ylabel('y_axis', size=10)

ax2.set(xlim=[0.,5.], ylim=[-0.5,2.5], title="Sample", xlabel="x label", ylabel=" y label") # 이 경우 사이즈 지정 못함

plt.show()