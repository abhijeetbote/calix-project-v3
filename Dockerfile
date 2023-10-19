# Use the official Python image from Docker Hub
FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT ["python", "app.py"]