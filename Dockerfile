FROM ubuntu:16.04

MAINTAINER Chris Kretler <ckretler@umich.edu>

RUN apt-get update \
	&& apt-get install -y python python-pip host \
	&& pip install requests && pip install pool

RUN apt-get install net-tools

WORKDIR /app/

COPY . /app/

CMD ["python", "multithreaded_pinger.py"]