# 초를 받아서 몇시간, 몇분, 몇초인지 출력하자
# ex) 3989초는 1시간 6분 29초이다.

time = int(input("초를 입력하세요 >> "))

h = time // (60*60)

res = time % (60*60)

m = res // 60

s = res % 60

print("{0} 초는 {1}시간 {2}분 {3}초 입니다." .format(time, h, m, s) )
