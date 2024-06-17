# 클래스 메서드

# 객체를 생성하지 않아도 static 처럼 바로 사용 가능

# static 과 다른점은 cls 라는 인자가 더 추가된다. (cls 는 클래스를 가리킨다.)

# @classmethod 라는 데코레이터를 사용

# 주로 클래스 변수를 조작하거나 생성자 대신 클래스를 초기화하는데 사용

class Calc : 
    @staticmethod
    def plus(a, b) : 
        return a + b
    
    def minus(self, a, b) :
        return a - b

    @classmethod
    def multi(cls, a, b) :
        return a * b
    
    # 보통 자체 상태를 수정하거나 접근할때 사용
    count = 0
    @classmethod
    def countup(cls) :
        cls.count += 1
        
if __name__ == "__main__":
    # 스테틱은 객체 생성 없이 호출 가능
    print("{0} + {1} = {2}" .format(3, 5, Calc.plus(3, 5)))
    
    # 인스턴스는 객체 생성 후 호출 가능
    c = Calc()
    print("{0} - {1} = {2}" .format(7, 5, c.minus(7, 5)))
    
    # 클래스 메서드도 스테틱처럼 바로 호출 가능
    print("{0} * {1} = {2}" .format(7, 5, Calc.multi(5, 2)))
    
    # countup 메서드를 실행할 때마다 count 가 1 씩 증가
    Calc.countup()
    print(Calc.count)



