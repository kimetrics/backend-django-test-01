import multiprocessing
from os import environ as env


bind = '0.0.0.0:{}'.format(env.get('PORT', '8080'))
workers = multiprocessing.cpu_count() * 2 + 1
