"""
forloop 을 제어하는 기능
break- forloop block을 완전히 빠져 나오는것
continue- forloop block에 있는 코드들 무시하기
"""
dummy=0
for i in range(4):
    if(i==0):
        continue
    i+1
    dummy+=i
    None

fruits = ["사과", "바나나", "딸기"]
for fruit in fruits:
    #print(fruit)
    None

for i in range(2,10):
    for j in range(1,10):
        print(f"i:{i} * j:{j} = {i*j}")
        None
    None
