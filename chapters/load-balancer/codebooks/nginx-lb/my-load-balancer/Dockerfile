FROM nginx:alpine
FROM python:3.9-alpine

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt

COPY nginx.conf /etc/nginx/nginx.conf