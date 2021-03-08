import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pymysql

class MyManager:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
        self.curs = self.conn.cursor()
    
    def __del__(self):    
        self.conn.close()

    def getPrices(self,s_name):
        sql = "select s_price,in_time from stock WHERE s_name = '"+s_name+"' order by in_time desc  "
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        prices = []    
        for row in rows :
            prices.append(row[0])
        return prices
    

mm = MyManager()
fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.array([0,0,0,0,0,0])
y = np.array([0,1,2,3,4,5])


z1 = np.array(mm.getPrices("삼성전자"))
z2 = np.array(mm.getPrices("LG"))
z3 = np.array(mm.getPrices("SK"))

ax.plot(x   , y, z1)
ax.plot(x+1 , y, z2)
ax.plot(x+2 , y, z3)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()