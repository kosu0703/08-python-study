# 문자열 포맷 

# %s : str
# %d : int
# %f : float

# 숫자 - int
print("제 나이는 %d 입니다." %20)
print("제 나이는 %d 입니다." %20.45)
print("제 나이는 %d 입니다." %20.57)
print('ㅡ' * 30)

# 숫자 - float (소숫점 아래 6개가 나오므로 잘 안쓴다.)
print("제 나이는 %f 입니다." %20)
print("제 나이는 %f 입니다." %20.45)
print("제 나이는 %f 입니다." %20.57)
print('ㅡ' * 30)

# 숫자 자리 지정
print("제 나이는 %5d 입니다." %20)          # 다섯자리를 차지하고 오른쪽으로 붙는다.
print("제 나이는 %3d 입니다." %2453486432)  # 자리가 넘치면 그대로 표시된다.

print("제 나이는 %.1f 입니다." %20.45) # 20.4
# 파이썬은 기본적으로 '반올림 반짝' 방식을 사용하지 않고, 
# '짝수를 선호하는' 반올림을 해요. 
# 이를 round half to even 또는 bankers' rounding이라고 부르죠. 
# 이 방식은 반올림할 숫자가 정확히 중간값일 때, 
# 즉 1.5나 2.5처럼 0.5로 끝날 때, 가장 가까운 짝수로 반올림을 하게 되요.      

print("제 나이는 %.3f 입니다." %20.45)      # 모자른건 0 으로 채운다.
print("제 나이는 %.3f 입니다." %20.5678)    # 소숫점 셋째자리까지 (반올림 됨)

print("제 나이는 %10.4f 입니다." %3.145)    # 전체길이 10개이면서, 소숫점 넷째자리까지 표시

print('ㅡ' * 30)

age = 34
name = "고길동"
print("저의 이름은 %s 입니다\n저의 나이는 %d 입니다.\n저의 키는 %.1f 입니다." %(name, age, 181.2504))
print('ㅡ' * 30)

print("제 이름은 {} 입니다" .format(name))
print("제 나이는 {} 입니다" .format(age))
print("제 키는 {:.1f} 입니다" .format(181.2504))
print('ㅡ' * 30)

print("제 이름은 {0} 이고\n제 나이는 {1} 이고\n제 키는 {2:.1f} 입니다" .format(name, age, 181.2504))
print('ㅡ' * 30)



