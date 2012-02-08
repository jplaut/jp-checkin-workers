from os import environ
from pyres.worker import Worker
from pyres import ResQ
import redis
from tasks import *

redisHost = environ.get("REDIS_QUEUE_HOST")
redisPort = int(environ.get("REDIS_QUEUE_PORT"))
redisPassword = environ.get("REDIS_QUEUE_PASSWORD")

redisObject = redis.Redis(host=redisHost, port=redisPort, password=redisPassword)

r = ResQ(redisObject)
w = Worker(r)
w.work()