#!/bin/sh

# Base image
FROM python:3.8

# File Author / Maintainer
MAINTAINER Petronilo

# Copy the current project directory to the container's app directory
COPY . /usr/src/app

# Set the cmd working directory to the project directory
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8000

# CMD ["./startup.sh"]
# ENTRYPOINT ["sh", "/usr/src/app/startup.sh"]
# CMD exec gunicorn djangoapp.wsgi:application --bind 0.0.0.0:8000 --workers 3
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
