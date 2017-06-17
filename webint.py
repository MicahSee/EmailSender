from flask import Flask, request, render_template, redirect, url_for
import json
import email_sender
import schedule_timeout
from celery import Celery

app = Flask(__name__)
celery_app = Celery('tasks', backend='amqp', broker='amqp://')

@celery_app.task
def queue():
    email_sender_object = email_template(recipient_email,subject,email_body)
    scheduler_object = scheduler(number_of_emails,delay)
    scheduler_object.schedule_email(email_sender_object.send())
    return

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=["POST"])
def post():
    global recipient_email = request.form['recipient_email']
    global subject = request.form['subject']
    global email_body = request.form['email_body']
    global number_of_emails = request.form['number_of_emails']
    global delay = request.form['delay']
    queue()
    return redirect(url_for('index'))
    #instantiate email object and start new celery task with rabbit-mq

if __name__ == "__main__":
    app.run(debug=True)
