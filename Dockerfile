FROM python:3.10-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]
