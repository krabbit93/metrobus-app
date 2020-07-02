FROM python:3.7.8-alpine3.12

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "sync.py"]