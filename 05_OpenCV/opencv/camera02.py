# openCV 로 이미지(영상) 불러오기(읽어오기)

import sys
import cv2

# 상대경로
img = cv2.imread('./images/cat.bmp', cv2.IMREAD_GRAYSCALE) # 흑백으로
# 절대경로
#img = cv2.imread('D:/kosu0703/08_python_study/05_OpenCV/opencv/images/cat.bmp')

if img is None :
    print('Image load error')
    sys.exit() # 프로그램 종료

# 타입과 모양을 알아야 AI 적용 가능
print(type(img)) # numpy.ndarray => 저장 가능
print(img.shape) # (480, 640, 3)

# 이미지 화면 출력
cv2.imshow('imshow', img)
cv2.waitKey() # 아무키나 누르면 창 닫아짐

# 자원처리
cv2.destroyAllWindows()