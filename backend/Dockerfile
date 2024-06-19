FROM python:3.12-alpine3.20

WORKDIR /usr/app/backend

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT [ "sh run.sh" ]