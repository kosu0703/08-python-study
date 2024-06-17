import matplotlib.pyplot as plt
import numpy as np

# 한글 깨짐 처리 
plt.rcParams["font.family"]="Malgun Gothic"
# False로 설정하면 Matplotlib이 마이너스 기호에 표준 ASCII 하이픈-마이너스 (-)를 사용
plt.rcParams['axes.unicode_minus'] =False
plt.rcParams["font.size"]= 10

fig = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

names = ["Python","Java","Spring","Flask"]
score = [155,301,125,98]


names2 = ["kor","eng","math"]
score2 = [ 250,180, 225]

#ax1.plot(names, score , color="#f00") # 꺽은선 그래프
#ax1plot(names2, score2 ) # 꺽은선 그래프

ax1.bar(names, score ) # 막대 그래프
ax2.bar(names2, score2)

ax1.set_title("sample")
ax1.set_xlabel("과목")
ax1.set_ylabel("점수")

ax2.set(title="sample2", xlabel="과목2",ylabel="점수2" )

plt.show()



