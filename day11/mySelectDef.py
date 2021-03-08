from mpl_toolkits.mplot3d import Axes3D
import pymysql
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


class MyManager :
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
        self.curs = self.conn.cursor()
       
    def __del__(self):
        self.conn.close()
        
    def getprices(self,s_name):
        sql ="select * from stock where s_name='"+s_name+"' order by in_time desc"
        self.curs.execute(sql)
        result = self.curs.fetchall()
        
        prices=[]

        for i in result:
            prices.append(i[0])
        return prices
    
if __name__ == '__main__':
    mm = MyManager()
    prices = mm.getprices("삼성전자")
    print(prices)
    prices = mm.getprices("LG")
    print(prices)