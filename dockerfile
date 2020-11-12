FROM ubuntu

ADD ./ ./

RUN apt update
RUN apt install python3

CMD ["python3","server.py"]