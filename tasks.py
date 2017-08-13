from celery import Celery
import os

broker_uri= 

celery_app = Celery('tasks', broker=broker_uri, backend=broker_uri )

celery_app.conf.task_serializer = 'pickle'
celery_app.conf.accept_content = ['pickle']


@celery_app.task
def queue(obj):
    obj.schedule_email()
    return
