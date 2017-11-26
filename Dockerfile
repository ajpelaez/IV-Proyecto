FROM ubuntu:16.04

MAINTAINER Antonio Jesus Pelaez Priego

WORKDIR /
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN git clone https://github.com/ajpelaez/IV-Proyecto.git
RUN cd IV-Proyecto/ && pip3 install -r requirements.txt
EXPOSE 80
CMD gunicorn --chdir /IV-Proyecto/FindBlaBlaCarBot -b 0.0.0.0:80 api:__hug_wsgi__ --log-level=debug --timeout=40
