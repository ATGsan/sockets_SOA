FROM python:3.8-slim

WORKDIR .
COPY server.py .

ENTRYPOINT ["python", "server.py"]

