FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install django && \
    apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

