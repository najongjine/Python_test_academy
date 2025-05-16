"""
함수는 다른함수를 호출할수 있다
"""
def test1():
    print(f"test1 함수에요")
    test2()

def test2():
    print(f"test2 함수에요")

"""
재귀호출. 어떤 함수가 자기 자신을 호출하는거
종료조건이 없으면, 무한실행하다가 메모리 터짐.
실무에선 재귀함수 안씀
"""
def test3(num):
    if num <=0:
       return
    print(f"test3 함수에요")
    num=-1
    test3(num)




