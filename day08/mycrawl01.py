from urllib.request import urlopen      #resquest
from bs4 import BeautifulSoup    #BeautifulSoup

html = urlopen("http://localhost:8081/HELLOWEB01/crawl.jsp")  

print(html)

bsObject = BeautifulSoup(html, "html.parser")  #parser : 변환해준다 (html)


print(bsObject) # 웹 문서 전체가 출력됩니다. 

# -> urlopen에 나오는 소스 가져옴

#  데이터만 가져오기, for문 으로 태그제거하고 가져오기 
title = bsObject.findAll('td')
print(title)     #이럴경우 태그도 같이나온다 

# 태그 제거하기 
for i in range(title.__len__()) :
    print(title[i].get_text())

