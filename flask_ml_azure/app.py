from tensorflow.keras.layers import TFSMLayer
import tensorflow as tf
from flask import Flask, request, jsonify

app = Flask(__name__)

def preprocessing(json_payload):
    sentences = json_payload['message']
    tensors = tf.constant(sentences, dtype=tf.string)
    tensors = tf.expand_dims(tensors, axis=-1)  # 텐서 형태를 (1, 1)로 맞춤
    return tensors

def postprocessing(json_payload, prediction_tensor):
    # prediction_tensor가 딕셔너리인지 확인
    if isinstance(prediction_tensor, dict):
        # 올바른 키를 사용하여 텐서를 가져옴
        prediction_tensor = list(prediction_tensor.values())[0]

    prediction = prediction_tensor.numpy()
    sentences = json_payload['message']
    response = {}
    d = {}
    for idx, sentence in enumerate(sentences):
        idx = tf.argmax(prediction[idx])
        d[sentence] = 'ham' if idx == 1 else 'spam'
    response['request'] = sentences
    response['response'] = d
    return response

@app.route("/")
def home():
    return "<h3>애저 파이프라인을 이용한 지속적 배포</h3>"

@app.route("/predict", methods=['POST'])
def predict():
    try:
        model = TFSMLayer('./saved_model', call_endpoint='serving_default')
        app.logger.info("모델 로드됨.")

        json_payload = request.json
        app.logger.info(f"JSON 페이로드: {json_payload}")

        preprocessed_data = preprocessing(json_payload)
        app.logger.info(f"전처리된 데이터: {preprocessed_data}")

        predictions = model(preprocessed_data)
        app.logger.info(f"예측 결과 타입: {type(predictions)}")  # 예측 결과의 타입을 로그에 기록
        app.logger.info(f"예측 결과: {predictions}")

        response = postprocessing(json_payload, predictions)
        return jsonify(response)

    except Exception as e:
        app.logger.error(f"예측 중 오류 발생: {e}")
        return jsonify({"error": "예측 실패"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
