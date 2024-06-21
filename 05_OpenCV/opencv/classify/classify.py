# classify
# caffemodel 에서 제공된 학습된 ai 모델 사용
# 사진에서 사물 분류 처리

# 분류할 사물의 종류는 클래스 파일에 이름이 1000개 작성되어 제공함
# classification_classes_ILSVRC2012.txt 파일

# 원래는 구글에서 다운받음
# - 학습모델(bvlc_googlenet.caffemodel)
# - 구성파일(deploy.prototxt)
# - 클래스 파일(classification_classes_ILSVRC2012.txt)

import numpy as np
import sys
import cv2

filename = 'beagle.jpg'

# 외부에서 파일의 이름을 받을 경우
if len(sys.argv) > 1 :
    filename = sys.argv[1]

img = cv2.imread(filename)
if img is None :
    print('Image Load Failed')
    sys.exit()

# 학습모델 불러오기
# cv2.dnn.readNet(모델, 구성요소)
net = cv2.dnn.readNet('bvlc_googlenet.caffemodel', 'deploy.prototxt')
if net.empty() :
    print('DNN Model Load Failed')
    sys.exit()

# 분류할 사물 이름이 등록된 클래스 이름 파일 읽기
classNames = None
with open('classification_classes_ILSVRC2012.txt', 'rt') as f :
    # 모두 읽어서 줄바꿈 제거 후 한줄씩 나눠서 리스트 만들기
    classNames = f.read().rstrip('\n').split('\n')

# 리스트로 만들어짐
#print(classNames)

# 모델 실행 (읽어들인 이미지 파일을 적용)
# cv2.dnn.blobFromImage(입력 영상, scalefactor, size, mean)
# scalefactor : 입력 영상 픽셀 값에 곱할 값 (기본값 1)
# size : 이미지 크기 / mean : 각 채널(BGR)에서 뺄 평균값
inputBlob = cv2.dnn.blobFromImage(img, 1, (224, 224), (104, 177, 123))
net.setInput(inputBlob, 'data')

# 실행해서 예측 결과 얻기
prob = net.forward()
#print(type(prob)) # numpy.ndarray
#print(prob.shape) # (1, 1000)

# 분류 결과 확인 출력
out = prob.flatten()       # 평탄화 작업 (1차원 배열 만들기)
classId = np.argmax(out)   # 가장 큰 값의 인덱스 얻기
confidence = out[classId]  # 해당 클래스의 확률값

txt = '%s (%4.2f%%)' % (classNames[classId], confidence * 100)
# 위치 좌표 (10, 30)
cv2.putText(img, txt, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
            0.8, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()














