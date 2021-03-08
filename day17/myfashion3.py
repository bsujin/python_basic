import matplotlib.pyplot as plt
from tensorflow import keras
import urllib

# url 가져오기 
url = '';
urllib.request.urlretrieve(url,'testget.jpg')

# 이미지 작게 출력해보기
fashion_mnist = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

fig, axes = plt.subplots(nrows=8, ncols=20)
ax = axes.ravel()

for i in range(160):
    image = x_train[i]
    ax[i].imshow(image, cmap='Greys')
    ax[i].set_xticks([])
    ax[i].set_yticks([])
    
plt.show()