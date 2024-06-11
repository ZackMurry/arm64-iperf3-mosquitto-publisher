FROM python:3.10.14-alpine
RUN apk add --update --no-cache iperf3
RUN pip install paho-mqtt
RUN pip install iperf3
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
CMD bash publish.sh

