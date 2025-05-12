number1=input("숫자 정수를 입력해 주세요: ")

"""
firewall 패턴. 예외사항들을 먼저 검사한후, 적합하지 않으면 쳐내버리기
"""
try:
    number1=int(number1)
except:
    print("입력된 값이 정수가 아닙니다")
    exit()

if(type(number1)!=int):
    print("입력된 값이 정수가 아닙니다")
    exit()
    
if(number1%2 == 0):
    print(f"입력값 {number1} 은 짝수입니다")
else:
    print(f"입력값 {number1} 은 홀수입니다")