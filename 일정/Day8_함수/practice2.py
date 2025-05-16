"""
List Dictionary 함수 만들기
정렬하기는 Day7 sort.py 에 기능이 있음
이걸 함수로 만들기
"""
def list_dict_sort(list1,keyname):
    for i in range(len(list1)):
        for j in range(len(list1)):
            try:
                if list1[j][keyname] > list1[j + 1][keyname]:
                    #예전값 저장하기
                    temp = list1[j]
                    # 서로의 위치 바꾸기
                    list1[j]=list1[j+1]
                    # 서로의 위치 바꾸기
                    list1[j+1]=temp
            except:
                None
    return list1

list1 = [
    {"제품": "뭐뭐1", "price": 1110},
    {"제품": "뭐뭐2", "price": 20},
    {"제품": "뭐뭐3", "price": 3005},
    {"제품": "뭐뭐4", "price": 400},
    {"제품": "뭐뭐5", "price": 5050},
]
list1=list_dict_sort(list1,"price")
print(list1)