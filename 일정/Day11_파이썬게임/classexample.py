class 클래스이름:
    def __init__(self, 내가원하는변수):
        self.내가원하는변수 = 1

"""
클래스는 캡슐화가 가능
"""
class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"{self.name}이(가) 공격했다! ⚔️")

class Hero2(Hero):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"{self.name}이(가) 공격했다! ⚔️")
class Hero3(Hero2):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"{self.name}이(가) 공격했다! ⚔️")

# 캐릭터 만들기
hero1 = Hero("아더", 100)
hero2 = Hero("린", 80)

# 행동하기
hero1.attack()
hero2.attack()

"""
클래스는 실제 상황으로 말하면,
파이썬이랑, 자바스크립트는 잘 안씀

이유가
1. 진짜 어려움
상속의 경우, 자식은 부모의 모든것을 다 물려받음. 문제가... 자식과 부모의 코드가 똑같은게 겹치면 어떻게 해석??
상속의 상속의 상속을 가면 코드해독 지옥임
잘못된 클래스 설계는 폭탄 그 자체임

2. 문법
자바같은 경우는 타입클래스와, 생성클래스가 다른경우 문법 완전히 달라짐

3. 오버라이딩, 오버로딩, 캐스팅 이런것들 작동방식이 너무 어려움
"""