# 명함 이미지 외각선 추출

import numpy as np
import sys
import cv2
import random

src = cv2.imread('./images/namecard1.jpg')
# 너비 높이 차원 (810, 1080, 3)
print(src.shape)
if src is None :
    print('이미지 없음')
    sys.exit()

#cv2.imshow('src1', src)

# 이미지 크기 줄이기
src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
#cv2.imshow('src2', src)

# 흑백으로 변환
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
#cv2.imshow('src_gray', src_gray)

# 가로 세로 구하기
h, w = src.shape[:2]

# 레이블링과 외각선 저장용 3차원 행렬 만들기
dst1 = np.zeros((h, w, 3), np.uint8) # 흑백으로 만듦
dst2 = np.zeros((h, w, 3), np.uint8) # (0~255)

# 이진화 처리
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_OTSU)

# 외각선 검출
contours1, _ = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours2, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


# 외각선 선 지정
for i in range(len(contours1)) :
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # drawContours(이미지, 외각선 정보, i, random_color, 외각선 두께)
    cv2.drawContours(dst1, contours1, i, random_color, 1)

# 외각선 선 지정
for i in range(len(contours2)) :
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # drawContours(이미지, 외각선 정보, i, random_color, 외각선 두께)
    cv2.drawContours(dst2, contours2, i, random_color, 1)

#cv2.imshow('dst1', dst1)
#cv2.imshow('dst2', dst2)


# 외각선 그리기
dst3 = np.zeros((h, w, 3), np.uint8) # (0~255)
for i in range(len(contours2)) :
    # 좌표값
    pts = contours2[i]

    # 랜덤색 지정
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # drawContours(이미지, 외각선 정보, i, random_color, 외각선 두께)
    cv2.drawContours(dst3, contours2, i, random_color, 1)

    # 면적이 너무 작은 객체는 제외 시키자
    if cv2.contourArea(pts) < 1000 :
        continue

    # 외각선 근사화 : 이미지에서 물체의 외곽선을 추출할때, 그 외각선을 단순화하여 저장하는 방법
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)

    # 닫혀진 다각형이 아니면 제외
    if not cv2.isContourConvex(approx) :
        continue

    # 사각형 외각선 그리기, 좌표 추출(투시 변환을 위해서)
    if len(approx) == 4 :
        # 외각선 그리기
        cv2.drawContours(dst3, contours2, i, random_color, 2)

        # 좌표 읽기
        # pts[:, :, 0] => 모든 좌표의 x 값 중
        # argmin() => 가장 작은 값을 가진 인덱스 => 왼쪽
        # argmin() => 가장 큰 값을 가진 인덱스 => 오른쪽
        p_Left = tuple(pts[pts[:, :, 0].argmin()][0])
        p_Right = tuple(pts[pts[:, :, 0].argmax()][0])

        # pts[:, :, 1] => 모든 좌표의 y 값 중
        p_Top = tuple(pts[pts[:, :, 1].argmin()][0]) # 가장 작은 값 => 위쪽
        p_Bottom = tuple(pts[pts[:, :, 1].argmax()][0]) # 가장 큰 값 => 아래쪽

        print(p_Left, p_Right, p_Top, p_Bottom)

cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)

cv2.waitKey()
cv2.destroyAllWindows()
