# 숫자형 : 정수, 실수, 복소수, 8진수, 16진수

# 1. 정수 : 소수점 아래가 없는 숫자
age = 28
print(age , type(age))

# 2. 실수 : 소수점 아래가 있는 숫자
weight = 92.4
print(weight , type(weight))

# 3. 실수형 지수 ( 컴퓨터식 지수 표현 )
height = 1.812E2    # 1.812 * 10^2
height2 = 3.1928e2     # 3.19 * 10^2
print(height , type(height))
print(height2 , type(height2))

# 4. 복소수 complex : 실수부 / 허수부
num = 412 + 34j
print(num , type(num))
# 실수부만 추출 (real)
print(num.real , type(num.real))
# 허수부만 추출 (imag)
print(num.imag , type(num.imag))

# 8진수 : 0o => 숫자 0 , 영어소문자 o 로 시작
# 0 1 2 3 4 5 6 7 그다음 8 이 되는 순간 10 이 된다.
# 즉 , 한자리에 8개만 표시
# 0 ~ 7 , 10 , 11 ~ 17 , 20 , ...
num = 0o10
print(num , type(num))

# 16진수 : 0x => 숫자 0 , 영어소문자 x 로 시작
# 0 ~ 9 까지 하고 a b c d e f 그다음 g 가 되는 순간 10 이 된다.
# 한자리에 16개만 표시
# 0 ~ 9 , a ~ f , 10 , 11 ~ 19 , 1a , 1b , 1c , 1d , 1e , 1f , 20 , ...
num = 0x10
print(num , type(num))

# 정수를 실수로 변환
print('ㅡ' * 30)
num = 27
res = float(num)
print(res , type(res))

# 실수를 정수로 변환
print('ㅡ' * 30)
num = 3.141592
res = int(num)
print(res , type(res))

# 반올림 안됨
num = 2.672
res = int(num)    
print(res , type(res))
# 반올림 되게
print('%.0f' %num)

# 소숫점 둘째자리 까지 구하기
print('ㅡ' * 30)
num = 27.444
res = int(num * 100) / 100
print(res , type(res))

# 반올림 되게
num = 27.445
print('%.2f' %num)

# 일의 자리 버리기
print('ㅡ' * 30)
num = 12345
res = int(num / 10) * 10
print(res , type(res))

