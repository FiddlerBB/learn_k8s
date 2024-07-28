FROM python:3.10-slim

COPY src/test_fast_api/requirements.txt .

COPY /src/test_fast_api/src /src

RUN pip3 install -r requirements.txt 

WORKDIR /src

CMD ["fastapi", "run", "main.py", "--port", "80"]
