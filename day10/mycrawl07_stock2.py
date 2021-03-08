from urllib.request import urlopen  # resquest
from bs4 import BeautifulSoup  # BeautifulSoup
import pymysql
import datetime

# db에 저장하기
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
curs = conn.cursor()

html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")  

print(html)

bs = BeautifulSoup(html, "html.parser")  # parser : 변환해준다 (html)

# class로 정보 가져오기 
tds = bs.select(".st2")

now = datetime.datetime.now()
in_time= now.strftime('%Y%m%d.%H%M')

# 세부적으로 정보 안에 필요한 정보만 추출하기 
for td in tds:
    
    # title가져오기 (a태그 안에 title ) 
    s_code = td.find(['a']).get('title')
    
    # 이름 가져오기 
    s_name = td.text
    
    # 가격 가져오기 
    s_price = td.parent.select("td")[1].text.replace(",","")
    
    # db에 저장하는 sql문 => 직접적으로 값을 넣어준다 (직관적) - 속도면에서는 %s와 차이 - 메모리 관리에는 %s가 더 용이하다 
    sql = "insert into stock(s_code, s_name, s_price, in_time) values("+s_code+","+s_name+","+s_price +","+in_time+")"
        
    print("code : ", s_code, end="  ")
    print("name : ", s_name, end="  ")
    print("price : ", s_price)

conn.commit()

# 확인되었나 조회하기 
sql = "select * from stock"
curs.execute(sql)
result = curs.fetchall()
print("sql저장완료 ")
print(result)

conn.close()
