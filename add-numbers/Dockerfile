FROM python:3.6-slim

RUN python -m pip install grpcio grpcio-tools

COPY add_numbers.py addnumbers_pb2.py addnumbers_pb2_grpc.py server.py  /app/
WORKDIR /app

CMD ["python", "server.py"]