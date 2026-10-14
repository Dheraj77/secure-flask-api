FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY access_control.py .

EXPOSE 5000

CMD ["flask", "--app", "access_control", "run", "--host=0.0.0.0"]