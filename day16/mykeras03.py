import cv2

img = cv2.imread('image/4.jpg', cv2.IMREAD_GRAYSCALE)

# 2차원 배열 
img2 = cv2.resize(img,(28,28))
print(img2)

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
