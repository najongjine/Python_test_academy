# input을 사용하면 키보드로부터 입력 받는다.
number1=input("숫자 정수를 입력해 주세요: ")

# try catch 예외처리기의 특징은 try block 안에 에러가 나도 except
# block을 실행함
try:
    #문자열을 정수로 강제 변환
    number1=int(number1)
    None
except:
    print(f"정수를 입력 안하셨네요")
    exit()

if(number1%2 == 0):
    print(f"입력값 {number1} 은 짝수입니다")
else:
    print(f"입력값 {number1} 은 홀수입니다")