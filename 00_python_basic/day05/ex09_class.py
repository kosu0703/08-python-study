class Calc :
    def add(self, s1, s2) :
        return s1 + s2
    
    def sub(self, s1, s2) :
        return s1 - s2
    
    def mul(self, s1, s2) :
        return s1 * s2
    
    def div(self, s1, s2) :
        return s1 / s2
    
calc = Calc()

while True :
    try: 
        su1 = int(input("수1 : "))
        su2 = int(input("수2 : "))
    except Exception :
        print("정수를 입력해 주세요")
        continue
    
    op = input("연산자 : ")
    if op not in ['+', '-', '*', '/'] :
        print("연산자를 제대로 입력하세요")
        continue
        
    res = 0
    if op == '+' :
        res = calc.add(su1, su2)
    elif op == '-' :
        res = calc.sub(su1, su2)
    elif op == '*' :
        res = calc.mul(su1, su2)
    elif op == '/' :
        try : 
            res = int(calc.div(su1, su2) * 100) / 100
        except Exception as e :
            print("0 으로는 나눌 수 없습니다.")
            continue
        
    print("{0} {1} {2} = {3}" .format(su1, op, su2, res)) 
    
    ans = input("계속할까요? (y/n) >> ")
    if ans.lower() == 'n' :
        break
    