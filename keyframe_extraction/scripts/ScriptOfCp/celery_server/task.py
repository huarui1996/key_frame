#!usr/bin/python 
#coding=utf-8 

import matlab.engine
from celery import Celery

from celery_server import celery_config
from redis_middle.redis_middle_class import Conn_db

redis_db = Conn_db()

app = Celery()
app.config_from_object(celery_config)
eng = matlab.engine.start_matlab()

print("MATLAB INIT FINISH")
print("MATLAB PATH %s" % (eng.cd()))

@app.task(queue='words')
def words(words):
    result = eng.get_info(words)
    return result
