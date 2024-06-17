# static 메서드

# 파이썬에서는 static 메서드를 @staticmethod 라는 데코레이터를 사용한다. 
#                                           (자바에서는 이노테이션)

# instance 메서드와 달리 self 가 없다.
# 객체를 생성하지 않아도 메서드 사용이 가능하다. => 클래스이름.메서드() 

class Calc :
    @staticmethod 
    def plus(a, b) :
        return a + b
    # 스테틱과 인스턴스의 차이점 (self)
    def minus(self, a, b) :
        return a - b

if __name__ == "__main__" :
    # 스테틱은 객체 생성 없이 호출 가능
    print("{0} + {1} = {2}" .format(3, 5, Calc.plus(3, 5)))
    
    # 인스턴스는 객체 생성 후 호출 가능
    c = Calc()
    print("{0} - {1} = {2}" .format(7, 5, c.minus(7, 5)))
    
    







