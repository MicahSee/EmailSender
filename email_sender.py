import smtplib

smtp_server =
port = 587
from_email =
email_pass = 

class email_template(object):
    def __init__(self,recipient,subject,body):
        self.recipient = recipient
        self.body = body
        self.subject = subject
    def send(self):
        server = SMTP(smtp_server,port)
        server.ehlo()
        server.starttls()
        server.login(from_email,email_pass)
        server.sendmail(from_email,self.recipient,self.body)
        return
