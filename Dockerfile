FROM python:3.12.11-slim

WORKDIR /app

COPY requirements.txt /app
RUN apt-get update -y && apt-get upgrade && pip install uv && uv pip install -r requirements.txt

COPY . /app

CMD ["python3", "main.py"]