FROM python:3.12.0

ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client \
    && apt-get install nginx -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/store

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x docker-entrypoint.sh

EXPOSE 8002

CMD ["./docker-entrypoint.sh"]
