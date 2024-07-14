FROM python:3.10-slim

COPY /src /src

COPY requirements.txt .

RUN pip install -r requirements.txt 

WORKDIR /src

CMD ["python", "-u", "main.py"]