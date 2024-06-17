# 다중 if 문

# if 조건식1 :
#       조건식1 이 참일때 실행
# elif 조건식2 :
#       조건식2 가 참일때 실행
# elif 조건식3 :
#       조건식3 이 참일때 실행
# else :
#       모두 거짓일때 실행 (즉, 나머지)

# 이름, 국어, 영어, 수학 점수를 받아서 총점, 평균, 학점을 구하자
name = input("이름 : ")
kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
math = int(input("수학 점수 : "))

total = kor + eng + math
avg = int(total / 3 * 100) / 100

hak = ""
if avg >= 90:
    hak = "A"
elif avg >= 80:
    hak = "B"
elif avg >= 70:
    hak = "C"
else:
    hak = "F"
    
print("ㅡ" * 30)
print("이름\t총점\t평균\t학점")
print(name , "\t" , total , "\t" , avg , "\t" , hak)
