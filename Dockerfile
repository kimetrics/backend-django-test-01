FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

CMD [ "gunicord", "-c", "config/gunicorn/conf.py", "--bind", ":8000","--chdir","src","src.pos.wsgi:application"]