FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install flask flask_cors requests gunicorn

EXPOSE 5004

CMD ["gunicorn", "main:app", "-w", "1", "--bind", "0.0.0.0:5004"]
