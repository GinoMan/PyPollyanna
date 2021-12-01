# Python Emailing Module
# Written by Gino Vincenzini
# Copyright 2021 Gino Vincenzini. Licensed under GPLv3

import configparser
import smtplib
import types
import typing
import re
import os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SMTPHandler:
    server = ""
    port = 0
    username = ""
    password = ""
    security = ""
    config: configparser.ConfigParser
    system: smtplib.SMTP
    
    def SendEmail(self, destination: str, content: str, txtcontent: str):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Polyanna Assignment for Christmas 2021"
        msg['From'] = self.username
        msg['To'] = destination
        if (txtcontent is not None):
            msg.attach(MIMEText(txtcontent, 'plain')) 
        if (content is not None):
            msg.attach(MIMEText(content, 'html')) 
        # self.system.set_debuglevel(1)
        self.system.sendmail(self.username, [destination], msg.as_string())
        
    
    def __init__(self, configFilePath: str):
        self.config = configparser.ConfigParser()
        self.config.read(configFilePath)
        self.username = self.config['DEFAULT']['Email']
        self.password = self.config['DEFAULT']['Password']
        self.server = self.config['DEFAULT']['SMTPServer']
        self.port = int(self.config['DEFAULT']['SMTPPort'])
        self.security = self.config['DEFAULT']['SMTPSecurity']
        
        # Setup the SMTP system.
        self.system = smtplib.SMTP(host=self.server, port=self.port)
        if self.security == 'TLS' and self.port != 25:
            self.system.starttls()
        self.system.login(self.username, self.password)
    
    def __del__(self):
        self.system.quit()
        del(self.system)
        
class TXTHandler:
    def SendEmail(self, destination: str, content: str, txtcontent: str):
        fileName = re.sub("@.*", "", destination)
        fileName += ".email.txt"
        outputDir = './OutputMessages'
        if not os.path.isdir(outputDir):
            os.mkdir(outputDir)
        fileName = os.path.join(outputDir, fileName)
        with (open(fileName, "w")) as email:
            email.write(f"Subject: Polyanna Assignment for Christmas 2021\n")
            email.write(f"From: Gino.F.Vincenzini@gmail.com\n")
            email.write(f"To: {destination}\n")
            email.write("\n")
            email.write("---TXT---\n")
            email.writelines(txtcontent.split('\n'))
            email.write("\n\n")
            email.write("---HTML---\n")
            email.writelines(content.split('\n'))
            email.write("\n\n")
            email.write("---END-OF-MESSAGE---\n")
            
        with (open(fileName, "r")) as txtfile:
            return txtfile.readlines()
        pass
    
    def __init__(self, configFilePath: str = None):
        pass
    
    def __del__(self):
        pass

class Email:
    Recipient = ""
    EmailContent = ""
    EmailTxtContent = ""
    EmailHandler: SMTPHandler
    
    def __init__(self, recipient, content, txtcontent, handler=None):
        self.Recipient = recipient
        self.EmailContent = content
        self.EmailTxtContent = txtcontent
        if handler is None:
            self.EmailHandler = SMTPHandler("creds.conf")
        else:
            self.EmailHandler = handler
    
    def SendEmail(self):
        return self.EmailHandler.SendEmail(self.Recipient, self.EmailContent, self.EmailTxtContent)
