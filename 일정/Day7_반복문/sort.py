"""
정렬하기
리스트에 있는 딕셔네리 데이터를 가격순으로 정렬하기(오름차순)
for i in range(len(list1)):
    for j in range(len(list1) - i - 1):
        if list1[j]["가격"] > list1[j + 1]["가격"]:
큰 데이터를 그냥 뒤로 밀어버리기
        """

list1 = [
    {"제품": "뭐뭐1", "가격": 1110},
    {"제품": "뭐뭐2", "가격": 20},
    {"제품": "뭐뭐3", "가격": 3005},
    {"제품": "뭐뭐4", "가격": 400},
    {"제품": "뭐뭐5", "가격": 5050},
]
for i in range(len(list1)):
    for j in range(len(list1)):
            try:
                if list1[j]["가격"] > list1[j + 1]["가격"]:
                    print(f"i:{i}  j:{j}")
                    #예전값 저장하기
                    temp = list1[j]
                    print(f"바뀌기전j : {temp}")
                    print(f"바뀌기전j+1 : {list1[j+1]}")
                    # 서로의 위치 바꾸기
                    list1[j]=list1[j+1]
                    print(f"j : {list1[j+1]}")
                    # 서로의 위치 바꾸기
                    list1[j+1]=temp
                    print(f"j+1 : {list1[j+1]}")
            except:
                None
for i in list1:
    #print(i)
    None

