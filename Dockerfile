FROM python:3.11

WORKDIR /complaints-microservice

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY /app app

COPY .env .

EXPOSE 8001

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0"]