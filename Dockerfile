FROM python:3.10.14-alpine
#RUN apk add --update --no-cache python3 iperf3 py3-paho-mqtt
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
CMD python3 ./publisher.py


