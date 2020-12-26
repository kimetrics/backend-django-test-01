import multiprocessing
from os import environ as env


bind = ':{}'.format(env.get('PORT', '8080'))
workers = multiprocessing.cpu_count() * 2 + 1
