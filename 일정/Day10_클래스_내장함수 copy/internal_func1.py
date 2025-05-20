"""
파이썬 자체에서나, 외부 모듈이
이미 만들어노은 놈
"""
# 가장 대표적
#print(f"")

"""
matplot 모듈을 설치했다고 치며ㅑㄴ
matplot 에서 pyplot을 갔다 쓰겠다
근데 이름이 기니깐 plt 라고 별명을 지었다
"""
#import matplotlib.pyplot as plt

#x=[1,2,3,4]
#y=[10,20,25,30]

#plt.plot(x,y)
#plt.title("샘플 그래프")
#plt.xlabel("x축")
#plt.ylabel("y축")
#plt.show()


"""
처음써본 외부모듈
matplotlib
이게 그래프 그려줘서 편함
5줄로 그래프 우와 편해~~~~
이걸로 주식사이트 만들어야!!!
아 망했네

이 그래프는 png 임
그래서 1초마다 업데이트 하는 그래프를 만들수 없음
"""

"""
외부모듈-
어떤 모듈을 쓰냐에 따라, 할수있는것과 없는것이 정해져버림
백화점 세트 모듈도 있음. 그러면 걱정근심 없음

반면, 그럴듯한 모듈도 있고, 도구들만 주고 내가 만들어야하는
모듈도 있음
"""

"""
크롤링 예제. 효율 극악. 최악의 모듈 사용 사례
BeautifulSoup 크롤링 안되기로 유명함
이게 껍데기는 되보여도 실제 해보면 안됨
"""
# pip install requests
import requests
from bs4 import BeautifulSoup

url="view-source:https://www.ggacademy.gg/valorant?utm_source=google&utm_medium=cpc&utm_campaign=GGA_sa&utm_content=valorant&utm_term=%EA%B2%8C%EC%9E%84%20%EC%95%84%EC%B9%B4%EB%8D%B0%EB%AF%B8&utm_source=google&utm_medium=cpc&utm_campaign=plus_acquisiton&utm_content=plus&utm_term=&utm_term=%EA%B2%8C%EC%9E%84%20%EC%95%84%EC%B9%B4%EB%8D%B0%EB%AF%B8&utm_campaign=GGA_lead_sa&utm_source=google&utm_medium=cpc&hsa_acc=7211757500&hsa_cam=21743422500&hsa_grp=175898310940&hsa_ad=733294927410&hsa_src=g&hsa_tgt=kwd-329298958724&hsa_kw=%EA%B2%8C%EC%9E%84%20%EC%95%84%EC%B9%B4%EB%8D%B0%EB%AF%B8&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=21743422500&gbraid=0AAAAACnrFcjFlYQ3EQ7pLG82EtF2X5KkB&gclid=CjwKCAjwravBBhBjEiwAIr30VDWos4gftAe8oBYW9zukfEt1qfvxdB3bZHNxeS9j2XSLJlG_TLYNoBoCqhQQAvD_BwE"
response = requests.get(url)
#BeautifulSoup 객체 생성
soup=BeautifulSoup(response.text,'html.parser')

print(soup.title.text)


"""
외부모듈들은 꼭 한계치 테스트 해봐야함
"""