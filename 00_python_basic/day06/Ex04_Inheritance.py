# 상속 : 어떤 클래스를 만들때 다른 클래스의 기능을 물려받을 수 있게 만드는 것
#       자식클래스가 부모클래스의 변수와 메서드를 마음대로 사용할 수 있다.

# 형식) class 클래스_이름(상속할_클래스_이름)

class Animal() : 
    def eat(self) :
        print("먹는다")
    def play(self) :
        print("운동한다")
        
# Animal 클래스를 부모로 가지는 Human 자식 클래스        
class Human(Animal) :
    def wave(self) : 
        print("손을 흔들다")
    
class Dog(Animal) :
    def wave(self) :
        print("꼬리를 흔들다")
        
if __name__ == "__main__":
    human = Human()
    human.eat()
    human.play()
    human.wave()
    
    print("ㅡ" * 30)
    
    dog = Dog()
    dog.eat()
    dog.play()
    dog.wave()
    
# end main
    










