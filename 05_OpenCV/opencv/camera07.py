# 레이블링

# 이미지 입력 => 그레이스케일로 입력
# => 이진화(검정, 흰색) : threshold()
# => 레이블링 : connectedComponentsWithStats()
# => 외각선 검출 : findContours()

import cv2
import sys
import numpy as np
import random

src = cv2.imread('./images/coins.png', cv2.IMREAD_GRAYSCALE)
if src is None :
    print('이미지 없음')
    sys.exit()

# 너비 높이 (246, 300)
#print('shape : ', src.shape)
h, w = src.shape[:2]
#print('h : {}, w: {}' .format(h, w))

# 3차원 행렬 만들기(기본값 0)
dst1 = np.zeros((h, w, 3), np.uint8) # 흑백으로 만듦
dst2 = np.zeros((h, w, 3), np.uint8) # (0~255)
#print(type(dst1)) # <class 'numpy.ndarray'>
#print(dst1)

# 이진화 처리(자동 임계값 처리)
_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)
# 이진화된 그림 보기
#cv2.imshow('dst', src_bin)

# 레이블링 : 흰색 영역별 픽셀에 랜덤값으로 색상을 만들어서 추출된 픽셀 위치에 색상 값 기록
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)
#print('cnt : ', cnt) # 구성 요소의 개수 : 16
#print('labels : ', labels)
#print('labels(shape) : ', labels.shape) # (246, 300)
# 각 구성 요소의 상태값(통계 정보) : 외곽좌표(0,0), 너비(300), 높이(246), 면적(51510 pixel)
#print('stats : ', stats)
#print('centroids : ', centroids) # 중심 좌표

for i in range(1, cnt) :
    # 랜덤하게 색 만들기
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # 레이블링을 위해 준비된 행렬에 추출된 코인(흰색 부분에 색칠하기)
    dst1[labels == i] = random_color

#cv2.imshow('dst', src_bin)
#cv2.imshow('dst1', dst1)

# 외각선 검출
# findContours(이미지, 외각선 검출 모드, 외각선 근사화 방법)
contours, _ = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# 외각선 선 지정
for i in range(len(contours)) :
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # drawContours(이미지, 외각선 정보, i, random_color, 외각선 두께)
    cv2.drawContours(dst2, contours, i, random_color, 1)

cv2.imshow('src', src)
cv2.imshow('dst', src_bin)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()




