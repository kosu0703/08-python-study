# if ~ else 문

# if 조건식 :
#    조건식이 참일때 실행
# else :
#    조건식이 거짓일때 실행

#   받은 점수가 80 이상이면 합격 , 아니면 불합격
su1 = int(input("점수를 입력하세요 >> "))

if(su1 >= 80):
    res = "합격"
else:
    res = "불합격"

print(res)

# 받은 숫자가 홀수인지 , 짝수인지 판별
su2 = int(input("숫자를 입력하세요 >> "))

if(su2 % 2 == 0):
    res = "짝수"
else:
    res = "홀수"
    
print(res)

