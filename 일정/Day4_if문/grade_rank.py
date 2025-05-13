grade1=input("숫자 정수를 입력해 주세요: ")

try:
    grade1=int(grade1)
except:
    try:
        grade1=float(grade1)
    except:
        print("입력된 값이 숫가 아닙니다")
        exit()
    
# 75 입력하면
"""
if(grade1>=90):
    print(f"A등급 입니다")
elif(grade1>=80):
    print(f"B등급 입니다")
elif(grade1>=70):
    print(f"C등급 입니다")
else:
    print(f"F등급 입니다")
"""

if(grade1>=90):
    print(f"A등급 입니다")
if(grade1>=80 and grade1<=89):
    print(f"B등급 입니다")
if(grade1>=70 and grade1<=79):
    print(f"C등급 입니다")
if(grade1<=60):
    print(f"F등급 입니다")

