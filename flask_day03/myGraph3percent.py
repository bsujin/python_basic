import pymysql
import matplotlib.pyplot as plt
import numpy as np
import time

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
        return  np.array(prices)
    
  
     

start = time.time()    
mm = MyManager()

fig = plt.figure()  # 3d그래프의 크기 
ax = fig.gca(projection='3d')
codes = mm.getAllScode()
print(len(codes))
   

zs = []
# s_code의 값을 넣어주기
cnt = 0
for code in codes: 
    cnt += 1
    print("순번 :", cnt, " scode :",code)
    zs.append(mm.getPricesPerNumpyFromCode(code))
#     zs.append(mm.getPricesPerNumpy("000020"))
#     zs.append(mm.getPricesPerNumpy("000100"))
#     zs.append(mm.getPricesPerNumpy("000105"))

            #  shapes
# x = np.array([0, 0, 0, 0, 0, 0])        -> row의 갯수를 넣어준다 
# y = np.array([0, 1, 2, 3, 4, 5])        -> 증가하는 배열을 만들어주는것 : for 문의 range

x = np.zeros(len(zs[0]))
y = np.array(range(len(zs[0])))

# print(x.shape)
# print(y.shape)



# plot이 줄 수를 나타내고, 시작점, 
for i,z in enumerate(zs):
    ax.plot(x+i, y, z)
#     ax.plot(x + 0, y, zs[0])
#     ax.plot(x + 1, y,zs[1])
#     ax.plot(x + 2, y, zs[2])
#    

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

end = time.time()

lapse = (end-start)

print ("시작시간 :", start, " 끝난시간 :", end)
print ("걸린시간 :", lapse)
plt.show()

