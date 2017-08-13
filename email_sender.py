from smtplib import SMTP
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

smtp_server = 
port = 587
default_from_email = 
default_email_pass = 

class email_template(object):
    def __init__(self,recipient,subject,body,**kwargs):
        self.recipient = recipient
        self.body = body
        self.subject = subject
        if 'from_email' and 'from_password' in kwargs:
            self.from_email = kwargs['from_email']
            self.from_password = kwargs['from_password']
        else:
            self.from_email = default_from_email
            self.from_password = default_email_pass
        self.msg = MIMEMultipart()
        self.msg['From'] = self.from_email
        self.msg['To'] = recipient
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(body,'plain'))
        self.text = self.msg.as_string()
    def send(self):
        server = SMTP(smtp_server,port)
        server.ehlo()
        server.starttls()
        server.login(self.from_email,self.from_password)
        server.sendmail(self.from_email,self.recipient,self.text)
        return
#include subject in email-sen
