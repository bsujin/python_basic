import tensorflow as tf
import cv2
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cloth.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img,(28,28))
img3 = 1 - (img2.reshape((1, 28 * 28))/ 255)
cv2.waitKey(0)
cv2.destroyAllWindows()

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)
# model.save("mymodel")
# evaluate() 손실(loss), 정확도(accuracy)를 얻음 
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print(test_loss, test_acc)
print("-----------------------------------")
print(img3)
print("----------------------------------")

# predict() : 모델이 각 이미지의 클래스를 예측하는 결과를 확인 
pre = model.predict(img3)
print(pre)
print("----------------------------------")
print('\nTest accuracy:', test_acc)
maxIdx = np.argmax(pre[0])
print("값이 일치하는 인덱스 : ",maxIdx)

# 이름을 출력 
print("인덱스의 값 : ",class_names[maxIdx])
