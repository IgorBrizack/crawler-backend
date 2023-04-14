FROM python:3.8-slim-buster

WORKDIR /app

RUN python3 -m pip install --upgrade pip

COPY . .

RUN pip install -r dev-requirements.txt

CMD ["python3",  "main.py"]