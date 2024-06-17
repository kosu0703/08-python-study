# 표준 라이브러리 : 파이썬을 설치할 때 자동으로 설치되는 라이브러리

import datetime, time, calendar
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)

# 두 날짜의 차이 
diff = day2 - day1
print(diff) # 477 days, 0:00:00
# 날짜만
print(diff.days) # 477

day = datetime.date(2024, 5, 8)
# 요일 0 부터 시작 ( 0 => 월, ... , 6 => 일 )
print(day.weekday()) # 2 => 수요일

print("ㅡ" * 30)

# time() : 1970-01-01 00:00:00 부터 현재까지 밀리초로 환산
print(time.time()) 
# localtime() : 년월일시분초 형태로 변경하는 함수
print(time.localtime()) 
# asctime(), ctime() : 튜플 형태로 날짜와 시간을 알아보기 쉽게 리턴
print(time.asctime(time.localtime(time.time())))
print(time.ctime())

print("ㅡ" * 30)

# 시간에 관련된 세밀한 표현
# time.strftime('출력할 형식 포맷코드', time.localtime(time.time()))

# 날짜
print(time.strftime('%x', time.localtime(time.time()))) # 05/08/24
# 시간
print(time.strftime('%X', time.localtime(time.time()))) # 10:05:39

print("ㅡ" * 30)

# 보통 반복문에서 일정한 시간 간격을 두고 실행할 때 : sleep
for i in range(10) :
    print(i, end=' ')
    #time.sleep(1) # 1초 쉬었다가
print()

print("ㅡ" * 30)

# calendar
# 달력 (반환값 업음)
calendar.prcal(2024)
# 5월만 (반환값 업음)
calendar.prmonth(2024, 5)
# 요일 ( 0 => 월요일)
print(calendar.weekday(2024, 5, 8))

print("ㅡ" * 30)









