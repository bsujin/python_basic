import pymysql
import matplotlib.pyplot as plt
import numpy as np

class MyManager:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
        self.curs = self.conn.cursor()
       
    def __del__(self):
        self.conn.close()
        
    def getPrices(self, s_name):
        sql = "select s_code, s_name, s_price, in_time from stock where s_name='" + s_name + "' order by in_time desc"
        self.curs.execute(sql)
        result = self.curs.fetchall()
        
        prices = []
        time = []

        for i in result:
            prices.append(i[2])
            time.append(i[3])   # 시간에 따른 값의 변화 
        return prices

#     def name :
        
    
mm = MyManager()
fig = plt.figure()  # 3d그래프의 크기 
ax = fig.gca(projection='3d')
   
x = np.array([0, 0, 0, 0, 0,     0, 0, 0, 0, 0,     0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0]) 
y = np.array([0, 1, 2, 3, 4, 5,]) 
# z = np.array([2,3,4,2,2,1])

z1 = np.array(mm.getPrices("삼성전자"))
z2 = np.array(mm.getPrices("LG"))
z3 = np.array(mm.getPrices("SK"))

# plot test data
# plot이 줄 수를 나타내고, 시작점, 
ax.plot(x, y, z1)
ax.plot(x + 1, y, z2)
ax.plot(x + 2, y, z3)

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
