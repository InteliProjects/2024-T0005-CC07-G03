FROM python:3.9

RUN apt-get update && \
    apt-get install -y pkg-config default-libmysqlclient-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "run.py"]