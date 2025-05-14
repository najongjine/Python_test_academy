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
    print(f"while 반복문 이에요 {dummy}")
    None