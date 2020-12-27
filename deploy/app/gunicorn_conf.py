import multiprocessing
from os import environ as env


bind = ':{}'.format(env.get('PORT', '8080'))
env_workers = env.get('GUNICORN_WORKERS', None)
workers = env_workers if env_workers else multiprocessing.cpu_count() * 2 + 1
