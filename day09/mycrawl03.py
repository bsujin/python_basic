from urllib.request import urlopen  # resquest
from bs4 import BeautifulSoup  # BeautifulSoup

html = urlopen("http://localhost:8081/HELLOWEB01/mycrawl")  
bs = BeautifulSoup(html, "html.parser")  # parser : 변환해준다 (html)

print(html)
print(bs)   # 로그인을 하지 않을경우 경고메세지, 로그인을 하면 나온다 


tds = bs.select("td")

# 태그 제거하기 
for i in tds:
    print(i.text)
    

# select 는  find 와 다르게 알아서 다 가져온다 select == find all

