import sys
import cv2

filename = './images/namecard1.jpg'

src = cv2.imread(filename)
if src is None :
    print('이미지 없음')
    sys.exit()

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()