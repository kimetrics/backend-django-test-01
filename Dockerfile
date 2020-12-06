FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
RUN mkdir /src

WORKDIR /src
COPY . /src/

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "src", "pos.wsgi"]
