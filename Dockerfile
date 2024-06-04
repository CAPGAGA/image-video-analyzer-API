FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt -y upgrade && \
    apt-get install -y gcc python3 python3-pip build-essential pkg-config ffmpeg libsm6 libxext6

WORKDIR /api

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .



