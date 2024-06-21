# DNN Face
# 딥러닝 AI 학습 모델 다운 받아서, 카메라 영상에서 얼굴 인식 처리

import numpy as np
import sys
import cv2

# caffemodel 에서 다운받은 것 (영상 이미지에서 얼굴 인식하는 모델)
model = 'res10_300x300_ssd_iter_140000_fp16.caffemodel'
config = 'deploy.prototxt'

# 카메라로 부터 객체 생성
cap = cv2.VideoCapture(0)
# 또는
#cap = cv2.VideoCapture()
#cap.open(0)
if not cap.isOpened() :
    print('Camera Open Failed')
    sys.exit()

# 학습 모델 불러오기
net = cv2.dnn.readNet(model, config)
if net.empty() :
    print('DNN Model Load Failed')
    sys.exit()

# 카메라에 영상 출력
while True :
    ret, frame = cap.read()
    if not ret :
        break
    
    # 좌우반전 => flip(이미지, 1)
    frame = cv2.flip(frame, 1)
    
    blob = cv2.dnn.blobFromImage(frame, 1, (300, 300), (104, 177, 123))
    net.setInput(blob)
    detect = net.forward()

    # 4차원을 2차원으로 변환하여 사용 (검출 정보만)
    detect = detect[0, 0, :, :]

    # 프레임 크기와 인식된 데이터 추출
    (h, w) = frame.shape[:2]

    # 얼굴 위치 계산 및 사각형 그리기
    for i in range(detect.shape[0]) :
        confidence = detect[i, 2]
        if confidence < 0.5 :
            break

        x1 = int(detect[i, 3] * w)
        y1 = int(detect[i, 4] * h)
        x2 = int(detect[i, 5] * w)
        y2 = int(detect[i, 6] * h)
    
        # 얼굴 위치에 초록색 사각형 선 표시
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0))
        
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27 :
        break

cap.release()
cv2.destroyAllWindows()

        
        
        





