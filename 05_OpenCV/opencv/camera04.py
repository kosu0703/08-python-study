import cv2

cap = cv2.VideoCapture('./multi/vtest.avi')

fps = round(cap.get(cv2.CAP_PROP_FPS)) # 초당 프레임의 수
delay = round(1000/fps)

while True :
    ret, frame = cap.read()
    edge = cv2.Canny(frame, 50, 150)

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if cv2.waitKey(delay) == 27 :
        break

cap.release()
cv2.destroyAllWindows()
