FROM python:3.9.18-alpine
LABEL authors="sardor"

ENTRYPOINT ["top", "-b"]

WORKDIR .

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

