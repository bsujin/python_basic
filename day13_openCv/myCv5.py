import cv2
 
# 이미지 읽기 - 흑백으로 가져오기 2

img = cv2.imread('2.png',cv2.IMREAD_COLOR)
height, width, channel = img.shape

matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
dst = cv2.warpAffine(img, matrix, (width, height))


# print(img)
print('shape',dst.shape)

# 이미지 화면에 표시
cv2.imshow('test', dst)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 