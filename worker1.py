from os import environ
from myres.worker import Worker
from tasks import *

Worker.run(['aggregate_checkins'], server=environ.get('REDIS_QUEUE_SERVER'), password=environ.get('REDIS_QUEUE_PASSWORD'))