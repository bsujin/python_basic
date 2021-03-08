from flask import Flask, Response, jsonify, render_template
from flask import request, json
import numpy as np
import pymysql

app = Flask(__name__)

class MyManager:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
        self.curs = self.conn.cursor()
       
    def __del__(self):
        self.conn.close()
        
    def getPrices(self, s_name):
        sql = "select s_price from stock where s_name='" + s_name + "' order by in_time DESC"
        self.curs.execute(sql)
        result = self.curs.fetchall()
        
        prices = []
    
        for i in result:
            prices.append(i[0])
             
        return prices
    
# 모든 코드 가져오기 
    def getAllScode(self):
        sql = "select s_code from stock GROUP BY s_code"
        self.curs.execute(sql)
        result = self.curs.fetchall()
        
        codes = []
    
        for i in result:
            codes.append(i[0])
             
        return codes
  
    def getPricesPer(self,s_name):
#         sql = "select MIN(in_time), s_price form stock where s_name='"+ s_name +"'order by in_time desc"
        sql = "select s_price,in_time  from stock where s_name='"+ s_name +"'order by in_time"
        self.curs.execute(sql)
        result = self.curs.fetchall()
       
        p_init = 0;
        prices = []
        
        for idx, row in enumerate(result):
            if idx==0:
                p_init = row[0]     #row[0]의 값을 넣어라 
            prices.append((row[0]/p_init)*100)   # 시간에 따른 값의 변화
                     
# prices.append(row[1]/result[0][1]*100)
        return prices
    
    def getPricesPerNumpy(self,s_name):
        sql = "select s_price,in_time  from stock where s_name='"+ s_name +"'order by in_time"
        self.curs.execute(sql)
        result = self.curs.fetchall()
       
        p_init = 0;
        prices = []
        
        for idx, row in enumerate(result):
            if idx==0:
                p_init = row[0]     #row[0]의 값을 넣어라 
            prices.append((row[0]/p_init)*100)   # 시간에 따른 값의 변화
                     
        return  np.array(prices)
    
    # s_code 값 가져오기 
    def getPricesPerNumpyFromCode(self,s_code):
#         sql = "select s_price,in_time  from stock where s_code ='"+ s_code +"'order by in_time LIMIT 6"
        sql = "select s_price,in_time  from stock where s_code ='"+ s_code +"'order by in_time"
        self.curs.execute(sql)
        result = self.curs.fetchall()
       
        p_init = 100;
        prices = []
        
        for idx, row in enumerate(result):
            if idx == 0:
                if row[0] > 0 :
                    p_init = row[0]     #row[0]의 값을 넣어라
                    
            per = (row[0]/p_init)*100
            
            if per == 0:
                per = 98
                
            prices.append(per)   # 시간에 따른 값의 변화
        return  prices
    

app = Flask(__name__)

@app.route("/chart.do")
def chart():
    mm = MyManager()
    codes = mm.getAllScode()
   
    zs = []
    # s_code의 값을 넣어주기
    cnt = 0
    for code in codes: 
        cnt += 1
        print("순번 :", cnt, " scode :",code)
        zs.append(mm.getPricesPerNumpyFromCode(code))
    
#     conn = pymysql.connect(host='localhost', user='root', password='java',
#                        db='python', charset='utf8')
#     curs = conn.cursor()
#     curs.execute("select emp_id,emp_nm,nick_nm from emp")
#     rows = curs.fetchall()
#     conn.close()
#     print(rows)
    print(zs[0][0])
    return render_template('chart.html',stock_list=zs, enumerate=enumerate)

if __name__ == "__main__":
    app.run()