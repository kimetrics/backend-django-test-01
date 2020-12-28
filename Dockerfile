FROM python:3.8-slim

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -r /requirements.txt

RUN apt-get update \
    && apt-get install -y supervisor

COPY deploy/app/pos.supervisor.conf /etc/supervisor/conf.d/pos.supervisor.conf
COPY deploy/app/gunicorn_conf.py /etc/gunicorn/gunicorn_conf.py
COPY deploy/app/entrypoint.sh /
COPY deploy/app/wait-for-it.sh /
RUN chmod +x /entrypoint.sh /wait-for-it.sh

WORKDIR /app
COPY ./src /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

ENTRYPOINT ["/entrypoint.sh"]
