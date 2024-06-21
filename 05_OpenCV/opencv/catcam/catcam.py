# 오버레이
# 증강현실 위에 하나의 레이어를 얹어 놓은 것

# 카메라를 통해 들어오는 영상에서 얼굴을 인식해서,
# 머리에 고양이 귀 그림을 오버레이 처리

# 프레임 위에 고양이 귀를 오버레이 처리하는 함수
def overlay(frame, cat, pos) :
    if pos[0] < 0 or pos[1] < 0:
        return

    if pos[0] + cat.shape[1] > frame.shape[1] or pos[1] - cat.shape[0] > frame.shape[0]:
        return

    sx = pos[0]
    ex = pos[0] + cat.shape[1]
    sy = pos[1]
    ey = pos[1] + cat.shape[0]

    img1 = frame[sy:ey, sx:ex]  # shape = (h, w, 3), 얼굴 픽셀을 슬라이싱해서 저장함
    img2 = cat[:, :, 0:3]  # 고양이 그림을 슬라이싱해서 저장 (고양이 그림 전체 선택임)
    alpha = 1. - (cat[:, :, 3] / 255.)  # shape = (h, w)

    # 고양이 귀 외 부분에 대한 투명도 처리 (얼굴이 가려지지 않게 함)
    img1[:, :, 0] = (img1[:, :, 0] * alpha + img2[:, :, 0] * (1. - alpha)).astype(np.uint8)
    img1[:, :, 1] = (img1[:, :, 1] * alpha + img2[:, :, 1] * (1. - alpha)).astype(np.uint8)
    img1[:, :, 2] = (img1[:, :, 2] * alpha + img2[:, :, 2] * (1. - alpha)).astype(np.uint8)

import numpy as np
import cv2
import sys

# 텐서플로우에서 제공하는 모델 다운
model = 'opencv_face_detector_uint8.pb'
config = 'opencv_face_detector.pbtxt'

# 카메라로 부터 객체 생성
cap = cv2.VideoCapture(0)
if not cap.isOpened() :
    print('Camera Open Failed')
    sys.exit()

# 학습 모델 불러오기
net = cv2.dnn.readNet(model, config)
if net.empty() :
    print('DNN Model Load Failed')
    sys.exit()

# 고양이 귀 그림 가져오기 (알파 채널 투명도)
cat = cv2.imread('cat.png', cv2.IMREAD_UNCHANGED)
if cat is None :
    print('Image Load Failed')
    sys.exit()

# 카메라에 영상 출력
while True:
    ret, frame = cap.read()
    if not ret :
        break

    frame = cv2.flip(frame, 1)

    blob = cv2.dnn.blobFromImage(frame, 1, (300, 300), (104, 177, 123))
    net.setInput(blob)
    detect = net.forward()

    # 4차원을 2차원으로 변환하여 사용 (검출 정보만)
    detect = detect[0, 0, :, :]

    # 프레임 크기와 인식된 데이터 추출
    (h, w) = frame.shape[:2]

    # 얼굴 위치 계산 및 사각형 그리기
    for i in range(detect.shape[0]):
        confidence = detect[i, 2]
        if confidence < 0.5:
            break

        x1 = int(detect[i, 3] * w)
        y1 = int(detect[i, 4] * h)
        x2 = int(detect[i, 5] * w)
        y2 = int(detect[i, 6] * h)

        # 고양이 귀
        fx = (x2 - x1) / cat.shape[1]
        cat2 = cv2.resize(cat, (0, 0), fx=fx, fy=fx)
        position = (x1, y1 - (y2 - y1) // 4)

        # 함수 생성
        overlay(frame, cat2, position)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27 :
        break

cap.release()
cv2.destroyAllWindows()


