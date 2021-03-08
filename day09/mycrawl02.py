from urllib.request import urlopen  # resquest
from bs4 import BeautifulSoup  # BeautifulSoup

html = urlopen("http://localhost:8081/HELLOWEB01/crawl.jsp")  

print(html)

bs = BeautifulSoup(html, "html.parser")  # parser : 변환해준다 (html)

tds = bs.findAll("td")

# 태그 제거하기 
for i in tds:
    print(i.text)
    

