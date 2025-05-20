"""
제품 클래스 만들기
제품의 이름, 가격, 유통기한, 유통기한 검사함수

from datetime import datetime

# 비교할 날짜 (문자열을 날짜로 변환)
target_date_str = '2024-05-05'
target_date = datetime.strptime(target_date_str, '%Y-%m-%d').date()

# 오늘 날짜
today = datetime.today().date()

# 비교
if target_date < today:
    print("날짜가 지났습니다.")
elif target_date == today:
    print("오늘입니다.")
else:
    print("아직 날짜가 지나지 않았습니다.")

"""
from datetime import datetime
class Product:
    # 데이터 정의
    def __init__(self, name, price,expiredate):
        self.name=name
        self.price=price
        self.expiredate=expiredate
    def check_expiredate(self):
        target_date = datetime.strptime(self.expiredate, '%Y-%m-%d').date()

        # 오늘 날짜
        today = datetime.today().date()

        # 비교
        if target_date < today:
            print("날짜가 지났습니다.")
        elif target_date == today:
            print("오늘입니다.")
        else:
            print("아직 날짜가 지나지 않았습니다.")

#객체. 진짜 사용하는놈은 요놈
product1 = Product("달걀",500,"2025-06-01")
product1.check_expiredate()