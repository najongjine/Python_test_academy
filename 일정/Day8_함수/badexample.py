"""
좋아, 함수 분리를 잘못하거나 공통 기능을 무분별하게 공유할 경우, 
프로그램이 아주 작은 수정 하나로 전체가 망가지는 예제를 만들어줄게. 
이건 전형적인 "전역 상태 공유 + 과도한 의존성 + 깊은 함수 호출"의 문제를 보여주는 사례야.
"""
# 모든 함수가 이 전역 변수를 사용함
config = {
    "discount_rate": 1  # 전역 설정
}

def calculate_discount(price):
    return price * config["discount_rate"]

def apply_discount(price):
    return price - calculate_discount(price)

def checkout(products):
    total = sum(apply_discount(p) for p in products)
    return total


products = [100, 200, 300]
print("최종 결제 금액:", checkout(products))


"""
함수 사용시 주의할점!!!
함수안에 함수 호출하기 남발하지 마세요
"""