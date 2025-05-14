fruits = ["사과", "바나나", "딸기"]
for fruit in fruits:
    #print(fruit)
    None

# range 는 내가 반복할 횟수를 정해줌
# i(forloop이 알아서 만든 변수) 는 0부터 시작
# forloop 이 알아서 만든 변수는 forloop 밖에서는 사용 금지
for i in range(5):
    #print("안녕", i)
    None

"""
while 문을 사용할땐 꼭 종료 조건을 사용해 주어야 한다
"""
dummy = 0
while dummy < 100:
    dummy+=1
    #print(f"while 반복문 이에요 {dummy}")
    None


"""
forloop 안에 또 forloop 이 있을수 있다
"""
for i_1 in range(2):
    #print(f"i_1: {i_1}")
    None
    for i_2 in range(3):
        #print(f"i_1: {i_1}, i_2:{i_2}")
        None

"""
forloop 는 자동화를 구현하는데 1등급으로 중요하다.
"""

"""
반복문 멈추기
"""
for i_1 in range(2000):
    if i_1 == 3:
        #print(f"{i_1} 에서 멈춤")
        break
    #print(f"{i_1}")
    None

"""
반복문 특정구간 건너뛰기
"""
for i_1 in range(3):
    if i_1 == 2:
        continue
    print(f"{i_1}")
    None

print("프로그램은 계속 실행됨")