# 메서드 오버라이딩 : 부모클래스의 메서드와 같은 이름으로 자식

class Animal() :
    name = "인간"
    
    def sound(self) :
        print("안녕하세요")
        
    def eat(self) :
        print("먹는다")
        
class Cat(Animal) :
    name = "삼색이"
    def sound(self) :
        #print("야옹~")
        pass
    
    def prn(self) :
        print(self.name)
    
class Dog(Animal) :
    def sound(self) :
        print("멍멍~")
    def prn(self) :
        #print(self.name)
        print(super().name)

if __name__ == '__main__':
    cat = Cat()
    cat.sound()
    cat.prn()
    
    print("ㅡ" * 30)
    
    # Dog 에 name 이 없어서 부모의 name 을 가져온다.
    dog = Dog()
    dog.sound()
    dog.prn()











