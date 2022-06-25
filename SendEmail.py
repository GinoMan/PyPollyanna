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
	config_file_path: str
	config: configparser.ConfigParser
	system: smtplib.SMTP
	connected: bool = False
	
	def __init__(self, configFilePath: str):
		self.config = configparser.ConfigParser()
		self.config.read(configFilePath)
		self.username = self.config['DEFAULT']['Email']
		self.password = self.config['DEFAULT']['Password']
		self.server = self.config['DEFAULT']['SMTPServer']
		self.port = int(self.config['DEFAULT']['SMTPPort'])
		self.security = self.config['DEFAULT']['SMTPSecurity']

	def __del__(self):
		self.connected = False
		self.system.quit()
		del(self.system)
		
	def SendEmail(self, destination: str, content: str, text_content: str):
		if not self.connected:
			self.Connect()
		msg = MIMEMultipart('alternative')
		msg['Subject'] = ("Pollyanna Assignment for "
		f"{self.config['FACILITATOR']['Event']}")
		msg['From'] = f"{self.config['FACILITATOR']['Name']} <{self.username}>"
		msg['To'] = destination

		if (text_content is not None):
			msg.attach(MIMEText(text_content, 'plain'))
		if (content is not None):
			msg.attach(MIMEText(content, 'html'))

		# self.system.set_debuglevel(1)
		self.system.sendmail(self.username, [destination], msg.as_string())

	def Connect(self):
		# Setup the SMTP system.
		self.system = smtplib.SMTP(host=self.server, port=self.port)
		if self.security == 'TLS' and self.port != 25:
			self.system.starttls()
		self.system.login(self.username, self.password)
		self.connected = True

	def TestConnection(self) -> tuple[bool, str]:
		try:
			with smtplib.SMTP(host=self.server, port=self.port,
				timeout=10) as smtp:
				if self.security == 'TLS' and self.port != 25:
					self.system.starttls()
				self.system.login(self.username, self.password)
				smtp.noop()

		except smtplib.SMTPConnectError as error:
			return False, f"{error.errno}: {error.strerror}\n" \
				f"{error.smtp_code}: {error.smtp_error}"

		except smtplib.SMTPException as error:
			return False, f"{error.errno}: {error.strerror}"
			
		return True, "OK"


class TXTHandler:
	config: configparser.ConfigParser
	username: str
	config_file_path: str
	
	def __init__(self, configFilePath: str = ""):
		self.config = configparser.ConfigParser()
		if configFilePath:
			self.config_file_path = configFilePath
			self.config.read(configFilePath)
			self.username = self.config['DEFAULT']['Email']
		else:
			self.username = "Facilitator@pollyanna.com"
	
	def __del__(self):
		pass

	def TestConnection(self):
		return True

	def SendEmail(self, destination: str, content: str, text_content: str):
		fileName = re.sub("@.*", "", destination)
		fileName += ".email.txt"
		outputDir = os.path.expanduser('~/OutputMessages')
		if not os.path.isdir(outputDir):
			os.mkdir(outputDir)
		fileName = os.path.join(outputDir, fileName)
		with (open(fileName, "w")) as email:
			# The next two lines need to be changed
			# to allow for other facilitators and events
			email.write("Subject: Pollyanna Assignment\n")
			email.write(f"From: {self.username}\n")
			email.write(f"To: {destination}\n")
			email.write("\n")
			email.write("---TXT---\n")
			email.writelines(text_content.split('\n'))
			email.write("\n\n")
			email.write("---HTML---\n")
			email.writelines(content.split('\n'))
			email.write("\n\n")
			email.write("---END-OF-MESSAGE---\n")
			
		with (open(fileName, "r")) as text_file:
			return text_file.readlines()


class Email:
	Recipient = ""
	EmailContent = ""
	EmailTextContent = ""
	EmailHandler: SMTPHandler
	
	def __init__(self, recipient, content, text_content, handler=None):
		self.Recipient = recipient
		self.EmailContent = content
		self.EmailTextContent = text_content
		if handler is None:
			self.EmailHandler = SMTPHandler("creds.conf")
		else:
			self.EmailHandler = handler
			
	def __str__(self):
		return f"To: {self.Recipient}\n{self.EmailTextContent}"
	
	def SendEmail(self):
		return self.EmailHandler.SendEmail(self.Recipient,
		self.EmailContent, self.EmailTextContent)
