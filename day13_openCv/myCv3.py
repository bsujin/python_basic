import cv2
 
# 이미지 읽기 - 흑백으로 가져오기 1
img = cv2.imread('2.png',cv2.IMREAD_GRAYSCALE)

# print(img)
print('shape',img.shape)

# 이미지 화면에 표시
cv2.imshow('test',img)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()

#  이미지 저장하기
cv2.imwrite('3.png', img)