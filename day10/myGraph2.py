import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pymysql

# make 3d axes
fig = plt.figure()   # 3d그래프의 크기 
ax = fig.gca(projection='3d')


conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')

curs = conn.cursor()

sql ="select * from stock where s_name='삼성전자' order by in_time desc"
curs.execute(sql)
result = curs.fetchall()
print(result)

prices=[]

#for문 으로 select 가져오기 
for i in range(len(result)):
    code = result[i][0]
    name = result[i][1]
    price = result[i][2]
    date = result[i][3]
#     print(code)
#     print(name)
#     print(price)

# test data 
x = np.array([0,0,0,0,0,0]) 
y = np.array([0,1,2,3,4,5]) 
z = np.array([2,3,4,2,2,1])

# plot test data
# plot이 줄 수를 나타내고, 시작점, 
ax.plot(x, y,z)
ax.plot(x, y,z)
ax.plot(x, y,z)

# print(ax.plot)
# print(ax)

# make labels
# ax.set_xlabel('동화약품')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')


# plt.show()
conn.close()