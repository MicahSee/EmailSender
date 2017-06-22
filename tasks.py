from celery import Celery
import os

broker_url = os.environ['REDIS_URL']


celery_app = Celery(app.name, broker=broker_url, backend=broker_url )

celery_app.config['task_serializer'] = 'pickle'
celery_app.config['accept_content'] = ['pickle']

@celery_app.task #move to execution by celery worker first
def queue(obj):
    obj.schedule_email()
    return
