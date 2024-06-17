class Person : 
    name = ''
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Pilot(Person) :
    gender = "남성"
    def job(self) :
        print("저의 직업은 조종사 입니다. 이름은 {0}, 나이는 {1}, 성별은 {2}" 
              .format(self.name, self.age, self.gender))
        
class Doctor(Person) :
    addr = "서울시 마포구"
    def play(self) :
        print("저의 직업은 피겨선수 입니다. 이름은 {0}, 나이는 {1}, 주소는 {2}"
              .format(self.name, self.age, self.addr))
        
man = Pilot('탑건', 26)
man.job()

woman = Doctor('김연아', 37)
woman.play()
                    

          
        
        
    
    
    

    
    
    
    
    
    
    
        