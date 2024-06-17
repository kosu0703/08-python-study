# while 문에서 맨 처음으로 되돌아가는 예약어 => continue

# 1 ~ 10 홀수 출력
su = 0
while su < 10 :
    su += 1  
    if su % 2 == 0 :
        continue
    print(su)


