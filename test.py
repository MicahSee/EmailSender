from celery import Celery

app = Celery("test", backend="amqp", broker="amqp://")

@app.task(ignore_result=True)
def hello():
	return "HELLO WORLD"
