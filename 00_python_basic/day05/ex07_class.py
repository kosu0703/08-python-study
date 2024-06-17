"""
    - 클래스는 객체를 만드는 설계도이다. (자바와 같은 의미)

    - 클래스 이름은 첫글자 대문자로 시작, 두단어 이상으로 만들때는 단어 첫글자 대문자
    
    <구조>
        class 클래스명 :
            변수
            생성자
            함수
    
    - self : 자기자신을 의미하는 예약어
        ** 인스턴스 변수에 접근하기 위해서 반드시 self 사용
        ** 메서드 호출 시 인스턴스 자신을 전달하기 위해서 반드시 self 사용

"""

# 생성자 없음
class Human :
    name = '둘리'
    age = 5
    
    def dis_print(self) :
        print("{0} 살 {1} 입니다" .format(self.age, self.name))

# 객체 생성
person = Human()

# 메서드 실행
person.dis_print()

print("ㅡ" * 30)

# 생성자 있음
class Human2 :
    def __init__(self, name, age) :
        self.age = age
        self.name = name
    
    def dis_print(self) :
        print("{0} 은 {1} 살 입니다." .format(self.name, self.age))

person2 = Human2('홍길동', 24)

person2.dis_print()

print("ㅡ" * 30)

class Human3 :
    name = '둘리'
    age = 7
    
    def __init__(self, name, age) :
        self.age = age
        #self.name = name
    
    def dis_print(self) :
        print("{0} 은 {1} 살 입니다." .format(self.name, self.age))

person3 = Human3('홍길동', 24)

person3.dis_print()

Human3('희동이', 3).dis_print()








print("ㅡ" * 30)






