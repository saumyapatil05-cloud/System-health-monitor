FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 procps
WORKDIR /app
COPY monitor.py .
CMD ["python3","monitor.py"]
