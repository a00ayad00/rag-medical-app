FROM python:3.12.11-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install uv && uv init && uv pip install -r requirements.txt --system --no-cache-dir

COPY . /app

CMD ["python3", "main.py"]