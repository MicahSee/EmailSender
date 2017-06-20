from flask import Flask, request, render_template, redirect, url_for
import json
from email_sender import email_template
from schedule_timeout import scheduler
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://'
celery_app = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery_app.conf.update(app.config)

@scheduler_object.schedule_email
@celery_app.task #move to execution by celery worker first
def queue():
    email_object.send()
    return

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=["POST"])
def post():
    recipient_email = request.form['recipient_email']
    subject = request.form['subject']
    email_body = request.form['email_body']
    number_of_emails = request.form['number_of_emails']
    delay_time = request.form['delay']

    global schedule_object
    global email_object
    schedule_object = scheduler(number_of_emails,delay_time)
    email_object = email_template(recipient_email,subject,email_body)

    queue.delay(recipient_email,subject,email_body,number_of_emails,delay_time)

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
