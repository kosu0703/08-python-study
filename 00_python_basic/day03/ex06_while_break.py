# 반복문을 탈출할 때 사용하는 예약어 => break

coffee = 10
money = 300
while money :
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피는 {}잔 입니다." .format(coffee))
    if coffee == 0 :
        print("커피가 다 떨어졌습니다. 판매종료합니다.")
        break
    
# if 문 안에서 break 를 하면 while 문을 빠져나간다.
    
print("ㅡ" * 30)

# 거스름돈
coffee = 10
while True :
    money = int(input("돈을 넣어주세요 >> "))
    if money == 300 :
        print("커피를 줍니다.")
        coffee -= 1    
    elif money > 300 :
        print("거스름돈 {} 을 주고 커피를 줍니다" .format(money-300))
        coffee -= 1
    else :
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
    
    print("남은 커피는 {}잔 입니다." .format(coffee))
    if coffee == 0 :
        print("커피가 품절입니다.")
        break 
    
print("ㅡ" * 30)
