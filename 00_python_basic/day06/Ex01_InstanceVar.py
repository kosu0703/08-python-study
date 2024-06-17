# 인스턴스 변수 : 일반 변수, 객체가 생성되면서 같이 생성되는 변수
#                  self 가 붙어있다.

class Person :
    # 해당 메서드가 None 을 반환한다는 의미
    def __init__(self, name, age) -> None :
        self.name = name
        self.age = age
        
    def prn(self) :
        print("이름 : " , self.name)
        print("나이 : " , self.age)
        
if __name__ == "__main__" :
    man  = Person('홍길동', 37)
    man.prn()
    
    woman = Person('황진이', 25)
    woman.prn()
    
        
        








