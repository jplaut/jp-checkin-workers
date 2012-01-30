import os
import ast

BROKER_URL = os.environ.get('BROKER_URL')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND')
CELERY_MONGODB_BACKEND_SETTINGS = ast.literal_eval(os.environ.get('CELERY_MONGODB_BACKEND_SETTINGS'))
CELERY_IMPORTS = os.environ.get('CELERY_IMPORTS')
CELERYD_CONCURRENCY = os.environ.get('CELERYD_CONCURRENCY')