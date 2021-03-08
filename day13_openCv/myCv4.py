import cv2
 
# 이미지 읽기 - 흑백으로 가져오기 2
# 빨간색일 경우 gb 부분을 0으로 세팅 

img = cv2.imread('2.png',cv2.IMREAD_COLOR)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# print(img)
print('shape',gray_img.shape)

# 이미지 화면에 표시
cv2.imshow('test', gray_img)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
  
# 이미지 다른 파일로 저장
cv2.imwrite('test2.png',img)