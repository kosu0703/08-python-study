import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

names = ["Python","Java","Spring","Flask"]
score = [155,301,125,98]


names2 = ["kor","eng","math"]
score2 = [ 250,180, 225]

#ax1.plot(names, score , color="#f00") # 꺽은선 그래프
#ax1plot(names2, score2 ) # 꺽은선 그래프

ax1.bar(names, score ) # 막대 그래프
ax2.bar(names2, score2)

ax1.set_title("sample")
ax1.set_xlabel("class")
ax1.set_ylabel("count")

ax2.set(title="sample2", xlabel="aaaa",ylabel="bbb" )

plt.show()



