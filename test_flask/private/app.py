import  os

import cv2.dnn
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import base64

app = Flask(__name__)
CORS(app, resources={r"/*" : {"origins" : ["http://127.0.0.1", "http://localhost:3000"]}})

# 절대 경로로 변경
base_dir = os.path.dirname(os.path.abspath(__file__))
model = os.path.join(base_dir, "..", "dnnface", "res10_300x300_ssd_iter_140000_fp16.caffemodel")
config = os.path.join(base_dir, "..", "dnnface", "deploy.prototxt")

# opencv 를 활용해서 dnn 네트워크를 로드
net = cv2.dnn.readNet(model, config)

@app.route("/")
def hello_world():
    return "Hello, World"

@app.route("/data", methods=['POST'])
def data():
    # 클라이언트에서 넘어온 frame 정보를 받기
    frame_data = request.json['frame']
    # , 마다 분리 (헤더부분과 바디부분을 구별하여 바디부분만 사용)
    _, encoded_image = frame_data.split(',')
    # 이미지 디코딩 된 데이터를 바이트배열에서 numpy 배열로 변환(cv2 로 읽기 위해)
    frame = np.frombuffer(base64.b64decode(encoded_image), dtype=np.uint8)
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

    # dnn 전처리
    blob = cv2.dnn.blobFromImage(frame, 1, (300, 300), (104, 177, 123))
    # 모델을 바탕으로 추론
    net.setInput(blob)
    # 실행
    detect = net.forward()
    # 높이 너비 추출
    (h, w) = frame.shape[:2]
    # 실행 결과를 가지고 필요한 부분 추출
    # detect[0번째 요소 선택, 얼굴 탐지 클래스의 결과 선택, :, :] => 2차원 배열 반환
    detect = detect[0, 0, :, :]

    for i in range(detect.shape[0]) :
        # 결과의 신뢰도 추출
        confidence = detect[i, 2]
        if confidence < 0.5 :
            break

        # 이미지 사각형 그리기 위한 좌표(좌상->우하)
        x1 = int(detect[i, 3] * w)
        y1 = int(detect[i, 4] * h)
        x2 = int(detect[i, 5] * w)
        y2 = int(detect[i, 6] * h)

        # 실제 그리기
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0))

    # 이미지를 jpg 형식으로 인코딩
    _, buffer = cv2.imencode('.jpg', frame)

    # 인코딩된 이미지 데이터를 base64 형식으로 변환하여 문자열로 디코딩
    # 클라이언트에 전달하기 위해서 JSON 형식으로 인코딩할 수 있도록
    processed_image = base64.b64encode(buffer).decode("utf-8")

    # 즉, 들어올때 decode , 나갈때 encode
    return jsonify({'processed_image' : processed_image})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
