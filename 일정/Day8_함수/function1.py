"""
함수 정의법

def 함수이름():
    실행할 코드
"""

def test1():
    print("test1 함수에요")

"""
메게변수를 받는다라고 합니다
"""
def test2(a,b):
    print(f"a: {a} + b:{b} = {a+b}")

"""
매개변수, 리턴값
재료를 받고, 결과가 튀어나옴(반환)
"""
def test3(a,b):
    result={"success":True,"data":None,"message":""}
    sum=0
    try:
        sum=a+b
        None
    except Exception as exception:
        result["success"]=False
        result["message"]=exception
        result["data"]=None
        None
    result["data"]=sum
    return result

return_value=test3(45,2)
print(return_value)