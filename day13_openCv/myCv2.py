import cv2
 
# 이미지 읽기
img = cv2.imread('rgb.png', 1)
# print(img)

# 파란색으로 만들기
# print(img[0][0][0])

# 검은색 - 다 0 
# 위에 배열만 255 : 파란색
# 전체 다 255 : 흰색 

img[0][0][0] = 255
img[0][0][1] = 255
img[0][0][2] = 255

img[0][1][0] = 255
img[0][1][1] = 255
img[0][1][2] = 255

img[1][0][0] = 255
img[1][0][1] = 255
img[1][0][2] = 255

img[1][1][0] = 255
img[1][1][1] = 255
img[1][1][2] = 255
 
 

print('shape', img.shape)



# 이미지 화면에 표시
cv2.imshow('Test Image', img)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 