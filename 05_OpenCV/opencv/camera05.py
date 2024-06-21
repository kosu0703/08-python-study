import sys
import cv2

# 카메라로 부터 객체 생성
cap = cv2.VideoCapture(0)
# 또는
#cap = cv2.VideoCapture()
#cap.open(0)

if not cap.isOpened() :
    print('카메라 확인필요')
    sys.exit()

# 동영상 저장을 위한 옵션들
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 코덱
out_frame = cv2.VideoWriter('out_frame.avi', fourcc, fps, (w, h))
out_edge = cv2.VideoWriter('out_edge.avi', fourcc, fps, (w, h))

# 매순간 프레임 처리 및 화면 출력
while True :
    ret, frame = cap.read()
    if not ret :
        break

    edge = cv2.Canny(frame, 50, 150)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    # 프레임을 각 VideoWriter 객체에 저장
    out_frame.write(frame)
    out_edge.write(edge)

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if cv2.waitKey(10) == 27 :
        break

# 자원 해제
cap.release()
out_frame.release()
out_edge.release()
cv2.destroyAllWindows()