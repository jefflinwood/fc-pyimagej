FROM python:3.9.18-bookworm

WORKDIR /flask-app

RUN apt update
RUN apt-get install g++
RUN apt-get install default-jdk maven -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000
CMD [ "python3", "app.py"]