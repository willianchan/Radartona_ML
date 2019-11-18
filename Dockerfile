FROM python:3.6-slim

EXPOSE 8080

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "./app.py"]