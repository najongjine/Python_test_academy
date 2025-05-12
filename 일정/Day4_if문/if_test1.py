# https://wildojisan.tistory.com/13

dummy=False

# if는 () 안에 값이 true 이거나 있으면 실행.
if(1<0):
    #print(f"여기는 if block")
    #print(f"dummy 의 값:{dummy}")
    None
else:
    #print(f"여기는 else block")
    #print(f"dummy 의 값:{dummy}")
    None


# elif 는 여러개중 조건에 맞는거만 실행
door=None
#door = input("1번, 2번, 3번 문 중 하나를 선택하세요: ")

if door == "1":
    print("🐉 드래곤이 있다!")
elif door == "2":
    print("💰 보물방이다!")
elif door == "3":
    print("🕳️ 함정에 빠졌다!")
else:
    print("❓ 그런 문은 없다!")

# 외부모듈. 랜덤의 숫자를 생성해 주는 모듈
import random

name = None
#name = input("당신의 이름은? ")
health = random.randint(1, 100)

print(f"{name}의 체력은 {health} 입니다!")

if health > 70:
    print("👊 몬스터를 무찔렀다!")
elif health > 30:
    print("😬 가까스로 도망쳤다.")
else:
    print("😵 기절했다.")


if(True):
    if(True):
        None
        if(True):
            None
    None



