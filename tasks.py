from celery import Celery
import os

broker_url = os.environ['REDIS_URL']


celery_app = Celery('tasks', broker=broker_url, backend=broker_url )

celery_app.conf.task_serializer = 'pickle'
celery_app.conf.accept_content = ['pickle']

@celery_app.task #move to execution by celery worker first
def queue(obj):
    obj.schedule_email()
    return
