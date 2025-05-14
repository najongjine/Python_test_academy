"""
소수 판별하기
소수는 1 하고 자기 자신만 나머지(%. mod 연산) 가 0이 된다.
"""

number1=3
b_prime=True
for i in range(number1-1):
    
    if number1 % (i+1) == 0 and :
        print(f"{number1} % {i+1}")    
        b_prime = False
if b_prime:
    print(f"{number1} 는 prime number 입니다")
else:
    print(f"{number1} 는 prime number 아닙니다")