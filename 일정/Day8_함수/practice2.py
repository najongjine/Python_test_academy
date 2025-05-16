"""
어떤 정수를 매게변수로 받으면, 
그 정수가 짝수인지 홀수인지 판별해주는 함수 만들기
리턴값 자료구조 {"success":... "data"... "message":...}
"""
def odd_even_decide(num):
    result={"success":True, "data":"", "message":""}
    try:
        num=int(num)
        if(num%2==0):
            result["data"]="짝수입니다"
        else:
            result["data"]="홀수입니다"
    except Exception as err:
        result["success"]=False
        result["data"]=""
        result["message"]=err
    return result

number1=input("정수를 입력하세요 : ")
result=odd_even_decide( number1)
print(result)