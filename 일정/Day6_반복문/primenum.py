
"""
dummy1=input("정수들 입력하세요")
정수가 아니면 다시 입력하게끔 하기
b_int = False
dummy1 이 데이터, input() 기능, int() 변환기능, 반복문
"""

b_repeat=True
dummy1=""
while(b_repeat):
    dummy1=input("정수를 입력하세요: ")
    try:
        dummy1=int(dummy1)
        b_repeat=False
        None
    except:
        b_repeat=True
        None
print(f"입력한 값 : {dummy1}")