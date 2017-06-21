import smtplib

smtp_server = 'smtp.gmail.com'
port = 587
from_email = 'exploretheworldofdell@gmail.com'
email_pass = '7428Micah1711'

class email_template(object):
    def __init__(self,recipient,body):
        self.recipient = recipient
        self.body = body
    def send(self):
        server = SMTP(smtp_server,port)
        server.ehlo()
        server.starttls()
        server.login(from_email,email_pass)
        server.sendmail(from_email,self.recipient,self.body)
        return
