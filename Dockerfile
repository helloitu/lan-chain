FROM python:3.11.6-slim-bullseye
WORKDIR /app
COPY main.py .
RUN apt update
RUN apt upgrade
RUN apt install -y build-essential python3-dev libnetfilter-queue-dev
RUN apt install -y libpcap0.8
RUN pip install scapy
RUN pip install NetfilterQueue
RUN chmod 777 main.py
RUN chmod +x main.py
CMD ["python", "main.py"]