import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')

curs = conn.cursor()
sql = """insert into sample(col01,col02,col03)
         values (%s, %s, %s)"""
curs.execute(sql, (4, 4, 4))
curs.execute(sql, (5, 5, 5))
conn.commit()
 
sql = "select * from sample"
curs.execute(sql)
result = curs.fetchall()
print(result)
 
conn.close()