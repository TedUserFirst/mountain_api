FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y vim

RUN mkdir /mountain
WORKDIR /mountain

COPY pip.requirements /mountain/
RUN pip install -r pip.requirements && rm -f pip.requirements

COPY ./mountain/ /mountain/

