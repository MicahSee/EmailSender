from smtplib import SMTP
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

smtp_server = 'smtp.gmail.com'
port = 587
from_email = 'exploretheworldofdell@gmail.com'
email_pass = '7428Micah1711'

class email_template(object):
    def __init__(self,recipient,subject,body):
        self.recipient = recipient
        self.body = body
        self.subject = subject
        self.msg = MIMEMultipart()
        self.msg['From'] = from_email
        self.msg['To'] = recipient
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(body,'plain'))
        self.text = self.msg.as_string()
    def send(self):
        server = SMTP(smtp_server,port)
        server.ehlo()
        server.starttls()
        server.login(from_email,email_pass)
        server.sendmail(from_email,self.recipient,self.text)
        return
#include subject in email-sen
