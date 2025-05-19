# 클래스(설계도) 선언
class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"{self.name}이(가) 공격했다! ⚔️")

# 캐릭터 만들기. 객체 만들기.
# 객체를 만들고 나서는 생성자 함수가 자동으로 발동됨.
hero1 = Hero("",0)
hero2 = Hero("린", 80)

# 행동하기
print(f"hero1: {hero1.name} {hero1.hp}")
print(f"hero2:{hero2.name} {hero2.hp}")


"""
그냥 이론만 보면 클래스 별거 없어보임
근데 실제로 써보면 이거 굉장히 어려움

클래스 이론에는 설계도, 인스턴스, 캡슐화, 정보은닉, 상속, 오버라이딩, 오버로딩
이렇게 미쳐돌아감

그래서 클래스 사용하려면 솔직히 저거 다 알아야함
웃긴게 뭐냐면 파이썬이랑, 자바스크립트, 타입스크립트 진영은 클래스 잘 안씁니다
자바,c#,c++,GDScript 여긴 클래스 필수임
"""

"""
클래스의 장점-캡슐화
1.어떤 추상화 대상의 데이터와, 그것을 처리하기위한 함수를 같이 묶을수 있다
2.이 클래스의 모든 기능을 자식한테 다 물려줄수 있다.
"""
class Person:
    def __init__(self, name, birthdate,money):
        self.name=name
        self.birthdate=birthdate
        self.money=money
        None
    def showname(self):
        print(f"나의 이름: {self.name}")
        None

class PersonChild(Person):
        def __init__(self, name):
            """
            부모에 똑같은 이름의 변수가 있으면, 자식은 오버라이딩
            """
            self.name=name
        None

person1=Person("부모","0101",99990)
child1=PersonChild("자식")

print(f"person1 : {person1.name} {person1.birthdate} {person1.money}")
print(f"child1 : {child1.name}  {person1.money}")
