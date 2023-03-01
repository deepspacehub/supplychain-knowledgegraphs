FROM python:3.9

RUN apt-get update && apt-get install -y nmap

COPY scanner.py .

CMD ["python", "scanner.py"]