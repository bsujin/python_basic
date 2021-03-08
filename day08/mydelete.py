import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')

curs = conn.cursor()
sql="delete from sample where col01 = %s"
curs.execute(sql,7)

sql = "select* from sample "
curs.execute(sql)
result = curs.fetchall()
print(result)


 
conn.commit()
conn.close()
