import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')

curs = conn.cursor()
sql = """update sample
         set col01 =7 
         where col01 = 1"""
curs.execute(sql)

sql = "select* from sample "
curs.execute(sql)
result = curs.fetchall()
print(result)

# sql="delete from sample where col01 = %s"
# curs.execute(sql,5)
 
conn.commit()
conn.close()
