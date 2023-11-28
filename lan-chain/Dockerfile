FROM python:3.11.6-slim-bullseye
WORKDIR /app
COPY __init__.py .
COPY lvv.bin .
COPY run.sh .
COPY ChatSimulator.py .
COPY main.py .
RUN apt-get update
RUN apt-get upgrade
RUN apt install sudo -y
RUN apt install -y build-essential python3-dev libnetfilter-queue-dev iptables
RUN apt install -y libpcap0.8
RUN pip install scapy
RUN pip install NetfilterQueue
RUN chmod 777 main.py
RUN chmod 777 run.sh
RUN chmod 777 lvv.bin
RUN chmod +x main.py
RUN chmod +x lvv.bin
RUN chmod +x run.sh
RUN useradd -ms /bin/bash user
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/user
RUN apt install -y iputils-ping traceroute
CMD ["bash", "run.sh"]