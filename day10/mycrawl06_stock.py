from urllib.request import urlopen  # resquest
from bs4 import BeautifulSoup  # BeautifulSoup

html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")  

print(html)

bs = BeautifulSoup(html, "html.parser")  # parser : 변환해준다 (html)

# class로 정보 가져오기 
tds = bs.select(".st2")

# 세부적으로 정보 안에 필요한 정보만 추출하기 
for td in tds:
    
    # title가져오기 (a태그 안에 title ) 
    s_code = td.find(['a']).get('title')
    
    # 이름 가져오기 
    s_name = td.text
    
    # 가격 가져오기 
    s_price = td.parent.select("td")[1].text
    s_price.replace(",","")

    print("code : ", s_code, end="  ")
    print("name : ", s_name, end="  ")
    print("price : ", s_price)
    

