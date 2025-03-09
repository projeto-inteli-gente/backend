FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git libpq-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8502

CMD ["uvicorn", "app:app", "--port=8502", "--host=0.0.0.0"]