
"""
dummy1=input("정수들 입력하세요")
정수가 아니면 다시 입력하게끔 하기
b_int = False
dummy1 이 데이터, input() 기능, int() 변환기능, 반복문
"""

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
"""
user_input=""
while True:
    try:
        user_input = int(input("정수를 입력하세요: "))
        break  # 올바른 정수가 입력되면 루프 종료
    except:
        print("유효한 정수가 아닙니다. 다시 입력해주세요.")

"""
입력 받은 값이 소수(prime number)인지 아닌지 판별해보기
소수는 1 하고 자기 자신외의 나머지값(mod 연산)이 0이 아니어야 한다.
user_input % 어떤숫자 != 0
for i in range(user_input):
    None
"""
b_prime=True
for i in range(user_input):
    if(i<=1):
        continue
    if(user_input % i == 0):
        b_prime=False
    None
if(b_prime):
    print(f"{user_input} 은 소수입니다")
else:
    print(f"{user_input} 은 소수가 아닙니다")