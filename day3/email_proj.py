import os
import pandas as pd
import smtplib,ssl
import hashlib
import maskpass
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python\n"


df=pd.read_csv('encry.csv')

files=os.listdir()
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "urstruelysalman@gmail.com"  # Enter your address
receiver_email =  'urstruelysalman@gmail.com'    #df['email']    # Enter receiver address
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

password = input()
cnt=0


for file in df['filename']:
    if file in files:
        filename = file
        if filename[11]!='.':
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            message.attach(part)
            text = str(message)

            cnt=cnt+1
            if(cnt==len(df['email'])):
                break

            string=file[:-4]
            #encrypt the string
            hash_func = hashlib.sha1()
            encoded=string.encode("utf-8")
            hash_func.update(encoded)
            messa = hash_func.hexdigest()
            text = text + "\n Hello I am salman and your password to open the file is\n" + messa + "\nHave a good day"
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email,df['email'].values(cnt), text)









