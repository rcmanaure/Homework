# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
# Copy and install the requirements.
COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt
# copy all files
COPY . .

# # copy entrypoint bash file
COPY ./entrypoint.sh /

# # execute the following then running container
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
