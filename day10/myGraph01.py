import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# make 3d axes
fig = plt.figure()   # 3d그래프의 크기 
ax = fig.gca(projection='3d')

# test data 
# 선형계수학 : 행렬을 쉽게 해주는것 -> np
# x = np.arange(-10, 10, 1) 

# 기존의 배열을 np.array로 바꿔준다 - 사용할 때에는 np배열로 바꿔줘야 한다 

x = np.array([0,0,0,0]) 
y = np.array([0,1,2,3]) 
z = np.array([2,3,4,2])

print("x:",x)
print(y)
print(z)

# z1 = x + y
# z2 = x * x
# z3 = -y * y


# plot test data
# plot이 줄 수를 나타내고, 시작점, 
ax.plot(x, y,z)
ax.plot(x+1, y,z)
ax.plot(x+2, y,z)


# print(ax.plot)
# print(ax)

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.show()