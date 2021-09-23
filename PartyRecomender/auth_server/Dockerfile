FROM python:3.8-slim-buster
ENV FLASK_APP=app:app
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt update && apt upgrade -y && apt install wget -y
COPY requirements.txt requirements.txt
EXPOSE 5000
RUN pip3 install -r requirements.txt
RUN mkdir -p ~/.postgresql && wget "https://storage.yandexcloud.net/cloud-certs/CA.pem" -O ~/.postgresql/root.crt && chmod 0600 ~/.postgresql/root.crt
COPY . .
CMD ["flask", "run"]