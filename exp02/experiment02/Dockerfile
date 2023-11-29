FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copy the entire directory into the container
COPY . /app

# Install Django (assuming dependencies are installed)
RUN pip install --upgrade pip && \
    pip install django &&  \
    pip install psycopg2  

# Run commands within the virtual environment
CMD ["/bin/bash", "-c", "source myenv/bin/activate && python manage.py runserver 0.0.0.0:8000"]
