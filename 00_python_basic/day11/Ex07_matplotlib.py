import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# ax.set_xlim([0., 10.]) # x축, 0-10까지 표현
# ax.set_ylim([-0.5, 2.5]) # x축, 0-10까지 표현
# ax.set_title("matplot sample", size=15)
# ax.set_xlabel('x_axis', size=10)
# ax.set_ylabel('y_axis', size=10)

ax.set(xlim=[0.,5.], ylim=[-0.5,2.5], title="Sample", xlabel="x label", ylabel=" y label") # 이 경우 사이즈 지정 못함

plt.show()