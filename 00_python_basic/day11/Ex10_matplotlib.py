import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

names = ["Python","Java","Spring","Flask"]
score = [155,301,125,98]


names2 = ["kor","eng","math"]
score2 = [ 250,180, 225]

ax1.plot(names, score , color="#f00") # 꺽은선 그래프
ax1.plot(names2, score2 ) # 꺽은선 그래프

ax1.bar(names, score ) # 막대 그래프
ax1.bar(names2, score2)

ax1.set_title("sample")
ax1.set_xlabel("class")
ax1.set_ylabel("count")
plt.show()



