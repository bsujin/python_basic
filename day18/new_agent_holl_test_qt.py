import numpy as np
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import Sequential
from collections import deque
from random import *
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# agent 안의 build_model을 가져온다
def build_model():
	model = Sequential()
	model.add(Dense(10, input_dim = 1, activation = 'relu', kernel_initializer = 'he_uniform'))
	model.add(Dense(10, activation = 'relu', kernel_initializer = 'he_uniform'))
	model.add(Dense(2, activation = 'linear', kernel_initializer = 'he_uniform'))
	model.compile(loss = 'mse', optimizer = Adam(lr = 0.001))
	return model

form_class = uic.loadUiType("holl.ui")[0]

# gameEnv
class WindowClass(QMainWindow, form_class) :
	def __init__(self) :
		self.score = 0
		self.seq = 0
		super().__init__()
		self.setupUi(self)
		self.hol.clicked.connect(self.hol_click)
		self.jjak.clicked.connect(self.jjak_click)

	def hol_click(self) :
		self.select(0)

	def jjak_click(self):
		self.select(1)

	def select(self, mine):
		model = build_model()
		model.summary()
		
		# 신경망에 넣어서 결과를 봐야하므로 numpy로 만든다 (주식 예제 생각하기)
		numpy_mine = np.array([mine])
		numpy_mine = np.reshape(numpy_mine, [1, 1])
		# 인공지능의 출력을 받는다 
		numpy_mine = np.float32(numpy_mine)
		# 내가 낸것도 컴퓨터가 만들어준다 
		q_values = model.predict(numpy_mine)
		com = np.argmax(q_values[0])
		
		self.seq += 1
		
		# 데이터 출력
		if mine == 0:
			self.myselect.setText("홀")
			print("홀")
		elif mine == 1:
			self.myselect.setText("짝")
		if com == 0:
			self.comselect.setText("홀")
			print("컴 : 홀")
		elif com == 1:
			print("컴 : 짝")
			self.comselect.setText("짝")

		# 결과 출력
		if mine == com :
			self.score += 1
			self.result.setText("이겼습니다.")
		else :
			self.result.setText("졌습니다.")
		
		self.jumsu.setText(str(self.score))
		self.sequence.setText(str(self.seq))
		
# 		
		
if __name__ == "__main__":
	app = QApplication(sys.argv) 
	myWindow = WindowClass() 
	myWindow.show()
	app.exec_()
