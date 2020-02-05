FROM python:3.6-slim

COPY requirements.txt /app/

RUN python -m pip install -r /app/requirements.txt

COPY DigitClassifier_pb2.py DigitClassifier_pb2_grpc.py digit_classifier.py qmnist_cnn.pt server.py /app/
WORKDIR /app

CMD ["python", "server.py"]
