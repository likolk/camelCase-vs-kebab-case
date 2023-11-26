FROM python:latest

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install django

# Expose the necessary port
EXPOSE 8000

# Run Django server directly
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
