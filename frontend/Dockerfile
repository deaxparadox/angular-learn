FROM node:20-alpine3.20

WORKDIR /use/app/frontend

COPY . .

RUN npm install

ENTRYPOINT [ "sh run.sh" ]