import numpy as np
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import Sequential
from collections import deque
from random import *


# agent 안의 build_model을 가져온다

def build_model():
	model = Sequential()
	model.add(Dense(10, input_dim = 1, activation = 'relu', kernel_initializer = 'he_uniform'))
	model.add(Dense(10, activation = 'relu', kernel_initializer = 'he_uniform'))
	model.add(Dense(2, activation = 'linear', kernel_initializer = 'he_uniform'))
	model.compile(loss = 'mse', optimizer = Adam(lr = 0.001))
	return model

if __name__ == "__main__":
	model = build_model()
	model.load_weights('save_model/mdl_origin.h5')  
# 	==> 지우면 교육시키지 않은 데이터가 나온다 
	
	# model의 구조를 출력해주는 명령어 
	model.summary()
	jumsu = 0
	
	# 비지니스 로직
	for i in range(50):
		mine = randint(0,1)
		
		# 신경망에 넣어서 결과를 봐야하므로 numpy로 만든다 (주식 예제 생각하기)
		numpy_mine = np.array([mine])
		numpy_mine = np.reshape(numpy_mine, [1, 1])

		# 인공지능의 출력을 받는다 
		numpy_mine = np.float32(numpy_mine)
		
		# 내가 낸것도 컴퓨터가 만들어준다 
		q_values = model.predict(numpy_mine)
		print(q_values)
		com = np.argmax(q_values[0])

		# 데이터 출력
		if mine == 0:
			print('mine: 홀',end=" ")
		elif mine == 1:
			print('mine: 짝',end=" ")
			
		if com == 0:
			print('com: 홀',end=" ")
		elif com == 1:
			print('com: 짝',end=" ")
			
		if mine == com :
			jumsu+=1
	
	print("jumsu:",jumsu)
