FROM python:3.8-slim
RUN apt update && apt install build-essential -y &&  apt-get install manpages-dev -y && \
    apt upgrade -y && apt install wget -y
COPY requirements.txt requirements.txt
EXPOSE 8000
RUN pip3 install -r requirements.txt
RUN mkdir -p ~/.postgresql && wget "https://storage.yandexcloud.net/cloud-certs/CA.pem" -O ~/.postgresql/root.crt && chmod 0600 ~/.postgresql/root.crt
COPY . .
CMD ["uvicorn", "recsys:app", "--host", "0.0.0.0", "--port", "8000"]