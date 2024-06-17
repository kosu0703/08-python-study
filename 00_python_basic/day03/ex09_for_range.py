# for 문과 함께 자주 사용하는 range 함수

su = range(10)
print(su) # range(0, 10) => 0 부터 10 까지 (10 포함 안함)

print(len(su)) # 10개 => 0 ~ 9

for i in su :
    print("i = " , i)
    
print("ㅡ" * 30)

# 5단 출력
for i in range(1, 10) :
    print("5 * {0} = {1}" .format(i, 5*i))
    
print("ㅡ" * 30)
    
# 구구단 출력
for i in range(2, 10) :
    print("ㅡ" * 30)
    print(i , "단")
    for j in range(1, 10) :
        print("{0} * {1} = {2}" .format(i, j, i*j))

print("ㅡ" * 60)

# 구구단 가로로 출력
for i in range(2, 10) :
    print(i , "단")
    for j in range(1, 10) :
        print("{0} * {1} = {2}" .format(i, j, i*j), end="   ") # 줄바꿈 안함
    print() # 줄바꿈

print("ㅡ" * 60)




