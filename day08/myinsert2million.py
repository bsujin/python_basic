import pymysql
import time
import datetime

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')

curs = conn.cursor()
sql = """insert into sample(col01,col02,col03)
         values (%s, %s, %s)"""
        
# 시작 시간 구하기 
start =time.time();
time.sleep(1);

for i in range(300000):  
    cnt = curs.execute(sql, (i, 1, 1))
#     print("cnt", cnt)
    
conn.commit()

# 끝나는 시간 구하기 
end = time.time();

# sql = "select * from sample"
# curs.execute(sql)
# result = curs.fetchall()

# 시분초 단위로 변환하기 - dateTime import 후 
sec = end - start
times = str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]

print("시작시간 : ", start)
print("끝나는 시간 : ", end)
print("time :",times)  # 현재시각 - 시작시간 = 실행 시간
# print(result)
 
conn.close()