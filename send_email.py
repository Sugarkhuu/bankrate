# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:28:42 2018

@author: Sugar2
"""


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import pdb
import smtplib
import config

class send:
    def __init__(self,df=None,t0=None,t1=None):


        mymsg = df.to_html()
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "There is a change!!! Previous %s and now %s" %(t0,t1)
        msg['From'] = config.From
        msg['To'] = config.To
        # msg['CC'] = config.To

        # Create the body of the message (a plain-text and an HTML version).
        # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        html = mymsg

        # Record the MIME types of both parts - text/plain and text/html.
        # part1 = MIMEText(text, 'html')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.

        # msg.attach(part1)
        msg.attach(part2)
        # Send the message via local SMTP server.
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(config.From, config.PASSWORD)
        try:
            mail.sendmail(config.From, config.mail_list, msg.as_string())
            print("Success: Email sent!")
        except: 
            print("Email failed to send.")
        mail.quit()


    # if __name__ == "__main__":
        # main()