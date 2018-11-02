#!/usr/bin/python
import urllib2
import pdb
import zipfile
import os
import errno
import shutil
import smtplib 
import smtplib 
import requests
import cgi
import json
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
form = cgi.FieldStorage()

dataset = json.loads(form.value)
urls=[]
urls.extend(dataset['urls'])
file_u=''

emails=[]
emails.append(dataset['email'])

for i in urls:
    d1=i.split('www.')
    file_u+=d1[1]+' '
    d2=d1[1].split('.com')[0]
    req = requests.get(i)
    req.encoding
    # print(req.text)
    filename = os.path.abspath("Exam_url_fetch/"+d2+".html")
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, "w") as f:
        html_data=u' '.join((req.text)).encode('utf-8').strip()
        f.write(html_data)
shutil.make_archive('Exam_url_fetch', 'zip', os.path.abspath('Exam_url_fetch'))
# Mail sending is happen below
fromaddr = "no-reply@shashikala.com"
toaddr = dataset['email'] 
# instance of MIMEMultipart 
msg = MIMEMultipart() 
# storing the senders email address   
msg['From'] = fromaddr 
# storing the receivers email address  
msg['To'] = toaddr 
# storing the subject  
msg['Subject'] = "Email with zip file as attachment"
# string to store the body of the mail 
body = "The attachment contains html data of "+file_u
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
# open the file to be sent  /home/halk/myproject
filename = "attachment.zip"
attachment = open(os.path.abspath('Exam_url_fetch.zip'), "rb") 
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
# encode into base64 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
# creates SMTP session 
s = smtplib.SMTP('smtp.sendgrid.net', 587) 
# start TLS for security 
s.starttls() 
# Authentication 
s.login('apikey', "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") 
# Converts the Multipart msg into a string 
text = msg.as_string() 
# sending the mail 
s.sendmail(fromaddr, [toaddr], text) 
# terminating the session 
s.quit()
print "Content-type: text/html\n"
print "\n\n"
print "<HTML>"
print "<HEAD>"
print "<TITLE>Test</TITLE>"
print "</HEAD>"
print "<BODY>"
print "<h1>Email sent sucessfully</h1>"
print "</BODY>"
print "</HTML>"