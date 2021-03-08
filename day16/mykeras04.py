import cv2

img = cv2.imread('image/4.jpg', cv2.IMREAD_GRAYSCALE)
# 2차원 배열 
img2 = cv2.resize(img,(28,28))
# print(img2)
img3 = 1 - (img2.reshape((1, 28 * 28))/ 255)

# print(img2.reshape((1, 28 * 28))/ 255)

# im3과 같은 형태를 넣어줘야 한다 - mykeras04camera 와 같은 배열값으로 바꿔준다  
print(img3)

for i in img2:
    for j in i:
        if j > 10 :
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()

cv2.imshow('Test Image',img)
cv2.waitKey(0)

cv2.destroyAllWindows()
