import cv2
# Helper libraries
import numpy as np
from tensorflow.python.keras.models import load_model

img = cv2.imread('sinbal.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img,(28,28))
img3 = 1 - (img2.reshape((1, 28 * 28))/ 255)
cv2.waitKey(0)
cv2.destroyAllWindows()

model = load_model("mymodel")
print("-----------------------------------")
print(img3)
print("----------------------------------")
# predict() : 모델이 각 이미지의 클래스를 예측하는 결과를 확인 
pre = model.predict(img3)
print(pre)
print("----------------------------------")
print(model.predict_classes(img3))

# 배열을 만들기
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# 최대 일치하는 인덱스 값 출력 
maxIdx = np.argmax(pre[0])
print("값이 일치하는 인덱스 : ",maxIdx)

# 이름을 출력 
print("인덱스의 값 : ",class_names[maxIdx])