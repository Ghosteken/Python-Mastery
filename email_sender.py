# go over to gmail and setup 2 factor authentication
# generate app password
# create funtion to send the mail


from email.message import EmailMessage
from app2 import email_password
import ssl
import smtplib

email_sender = 'aigberuan6@gmail.com'
email_password = email_password

email_receiver = 'sipijo5311@taobudao.com'
subject = 'i love learning'
body = ''''

im just having fun

'''

#create an instance of the email message lib

em = EmailMessage()
em['FROM'] = email_sender
em['TO'] = email_receiver
em['SUBJECT'] = email_sender
em.set_content(body) 

context= ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:

    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())
    