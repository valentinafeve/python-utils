#! /usr/bin/env python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email='serranopat@yandex.com'
password='serranopat2'
send_to_email='ruastabi@gmail.com'
subject='e-mail subject'
message='<!DOCTYPE html><html><head><title>This is a message</title></head><body><style type="text/css">	*{		padding: 0		color: white;		background: black;	}</style><a href="www.facebook.com">Just a test</a><div background=blue>	Hey, whats up</div></body></html>'

msg= MIMEMultipart()
msg['From']= email
msg['To']=send_to_email
msg['subject']=subject

msg.attach(MIMEText(message, 'plain'))

server= smtplib.SMTP('smtp.yandex.com',465)
server.starttls()
print(server.login(email,password))
text = msg.as_string()
for x in range(2):
	server.sendmail(email, send_to_email, text)

server.quit()