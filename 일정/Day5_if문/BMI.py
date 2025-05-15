"""
📌 BMI 계산기
조건:

사용자에게 키(cm)(데이터)와 몸무게(kg)(데이터)를 입력(기능)받아 BMI를 
계산한(기능) 후 등급을 출력(기능)
BMI = 몸무게 / (키(m) ** 2) (데이터 연산에 필요한 수학 수식)
키를 미터 단위로 변환:
170cm → 1.70m (즉, 170 ÷ 100) (데이터 연산에 필요한 수학 수식)
조건: (if 문제 들어갈 수학식)
BMI < 18.5: 저체중
18.5 ≤ BMI < 23: 정상
23 ≤ BMI < 25: 과체중
BMI ≥ 25: 비만
"""

height_cm=input("키cm 를 입력하세요: ")
height_cm=int(height_cm)
weight=input("몸무게 입력하세요: ")
weight=int(weight)
height_m = (height_cm / 100)
bmi=weight / (height_m ** 2)
print(f"bmi : {bmi}")

if bmi<18.5:
    print(f"저체중 입니다")
if 18.5<=bmi<23:
    print("정상 입니다")
if 23<=bmi<25:
    print("과체중 입니다")
if bmi>=25:
    print("비만 입니다")