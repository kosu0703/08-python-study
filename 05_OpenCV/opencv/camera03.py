import matplotlib.pyplot as plt
import cv2

# 컬러 영상
imgBGR = cv2.imread('./images/cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 흑백 영상
imgGray = cv2.imread('./images/cat.bmp', cv2.IMREAD_GRAYSCALE) # 흑백 필수1
plt.axis('off')
plt.imshow(imgGray, cmap='gray') # 흑백 필수2
plt.show()

# 두개 함께 출력
plt.subplot(121)
plt.axis('off')
plt.imshow(imgRGB)
plt.subplot(122)
plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()
