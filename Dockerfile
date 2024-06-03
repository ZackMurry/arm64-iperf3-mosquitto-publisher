FROM alpine:3.14
RUN apk add --update --no-cache iperf3 python3 py3-paho-mqtt && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
#RUN pip3 install --no-cache --upgrade pip setuptools
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
CMD ["/usr/bin/python", "/usr/src/app/publisher.py"]

