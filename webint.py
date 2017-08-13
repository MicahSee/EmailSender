from flask import Flask, request, render_template, redirect, url_for
from email_sender import email_template
from schedule_timeout import scheduler
from tasks import queue
import os

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.get('auth') == 'gmail':
        return render_template('gmail.html')
    else:
        return render_template('index.html')


@app.route('/post', methods=["POST"])
def post():
    recipient_email = request.form['recipient_email']
    subject = request.form['subject']
    email_body = request.form['email_body']
    number_of_emails = request.form['number_of_emails']
    delay_time = request.form['delay']

    email_object = email_template(recipient_email, subject, email_body)
    schedule_object = scheduler(number_of_emails, delay_time, email_object)

    queue.delay(schedule_object)

    return redirect(url_for('index'))


@app.route('/gmail_post', methods=["POST"])
def post_gmail():
    gmail_email = request.form['gmail_email']
    gmail_password = request.form['gmail_password']
    recipient_email = request.form['recipient_email']
    subject = request.form['subject']
    email_body = request.form['email_body']
    number_of_emails = request.form['number_of_emails']
    delay_time = request.form['delay']

    email_object = email_template(
        recipient_email, subject, email_body, from_email=gmail_email, from_password=gmail_password)
    schedule_object = scheduler(number_of_emails, delay_time, email_object)

    queue.delay(schedule_object)

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
