FROM ubuntu:16.04

MAINTAINER Antonio Jesus Pelaez Priego

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN git clone https://github.com/ajpelaez/IV-Proyecto.git
RUN cd IV-Proyecto/ && pip3 install -r requirements.txt
EXPOSE 80
WORKDIR IV-Proyecto/
CMD gunicorn --reload FindBlaBlaCarBot.api:__hug_wsgi__
