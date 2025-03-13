
FROM python:3.9-slim

WORKDIR /app

COPY secret.gz /app/
COPY templates/ /app/templates/
COPY server.py /app/

RUN pip install flask

EXPOSE 8000

CMD ["python", "server.py"]
