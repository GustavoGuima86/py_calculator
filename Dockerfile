FROM python:3.10-slim

WORKDIR /
COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8080
COPY / .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]