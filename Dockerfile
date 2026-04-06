FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY etl/requirements.txt etl/requirements.txt
RUN pip install --no-cache-dir -r etl/requirements.txt

COPY etl etl
COPY data data

ENTRYPOINT ["python", "etl/transform.py"]
CMD ["--input", "data/raw/patients.csv", "--output-dir", "data/clean"]
