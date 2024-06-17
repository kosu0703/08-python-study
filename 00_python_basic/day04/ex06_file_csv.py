# CSV : 쉼표(,) 로 구분한 텍스트 데이터 및 텍스트 파일

    # 확장자는 .csv 이며 MIME 형식은 text/csv 이다.

    # 첫번째 라인은 컬럼명이 나온다.

    # csv 파일은 보통 list 로 변환해서 처리한다.
    # 또는 딕셔너리로 변환해서 처리한다.

# 모듈 : 함수나 변수 또는 클래스를 모아 놓은 파일
import csv 

# 쓰기
f = open("day04/data/csv01.csv" , 'w' , encoding='utf-8' , newline='')
wr = csv.writer(f)

wr.writerow([1, "홍길동", 24, "서울"])
wr.writerow([2, "둘리", 7, "남극"])
wr.writerow([3, "임꺽정", 45, "대전"])

f.close()

# 읽기
f2 = open("day04/data/csv01.csv" , 'r' , encoding='utf-8')

rd = csv.reader(f2)

#print(rd, type(rd)) # 클래스 csv

# 수정을 위해서 리스트에 넣어서 처리하자
lines = []

for i in rd :
    # 성인, 미성년자
    if int(i[2]) <= 18 :
        #print("미성년자")
        i[2] = "미성년자"
    else :
        #print("성인")
        i[2] = "성인"
    lines.append(i)

f2.close()

#print(lines) # 리스트 안에 리스트

# 변경된 내용을 다시 쓰기
f3 = open("day04/data/csv01_e.csv" , 'w' , encoding='utf-8', newline='')

wr = csv.writer(f3)
wr.writerows(lines)

f3.close()

print("ㅡ" * 30)

# 추가하기
f4 = open("day04/data/csv01.csv" , 'r' , encoding='utf-8')

rd = csv.reader(f4)

lines2 = []

for i in rd :
    # 성인, 미성년자
    if int(i[2]) <= 18 :
        i.append("미성년자")
    else :
        i.append("성인")
    lines2.append(i)

f4.close()

# 변경된 내용을 다시 쓰기
f5 = open("day04/data/csv01_f.csv" , 'w' , encoding='utf-8', newline='')

wr = csv.writer(f5)
wr.writerows(lines2)

f5.close()






