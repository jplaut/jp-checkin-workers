from os import environ
from pyres.worker import Worker
from tasks import *

w = Worker(['aggregate_checkins'], server=environ.get('REDIS_QUEUE_SERVER'), password=environ.get('REDIS_QUEUE_PASSWORD'))
w.work()