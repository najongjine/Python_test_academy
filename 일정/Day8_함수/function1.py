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
#print(return_value)



"""
매개변수의 특징
"""
def swapnumber(a,b):
    temp = a
    a=b
    b=temp

number1=1
number2=2
#swapnumber(number1,number2) 함수로 할수 없는 작업

temp=number2
number2=number1
number1=temp
#print(f"number1:{number1}, number2:{number2}")

"""
Scope
이렇게 블록 안에 선언된 것들은, 해당 블록을 다 실행하고 나면
컴퓨터가 지워버림
if(){
}
try{}
function(){
}
"""
# 파이썬은 scope이란게 해당이 안되지만, 다른언어는 scope이라는 법칙에 의해
# 서로 다른 변수로 인식함
if (True):
    a=1
    b=2
a=11


"""
매게변수는 call by value, call by reference 가 있다
call by value는 int, float, string, bool
call by reference는 list, class
"""
# 진짜 객체의 주소로 받음
def add_item(my_list):
    my_list.append(4)

# 용량이 100mb
lst = [1, 2, 3]
add_item(lst)
print(lst)
