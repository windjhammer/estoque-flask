FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb3 \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

