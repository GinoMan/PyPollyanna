# PyPollyanna Emailing Module
# Written by Gino Vincenzini
# Copyright 2021 Gino Vincenzini. Licensed under MIT License

from abc import ABCMeta, abstractmethod
from re import sub
from os import mkdir
from os.path import expanduser, isdir, join
from configparser import ConfigParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPConnectError, SMTPException
from typing import Optional


class EmailHandler (metaclass=ABCMeta):
	@abstractmethod
	def __init__(self, configFilePath: str) -> None:
		pass
	
	@abstractmethod
	def __del__(self) -> None:
		pass
	
	@abstractmethod
	def SendEmail(self, destination: str, content: str,
		text_content: str) -> list[str]:
		return []

	@abstractmethod
	def Connect(self) -> None:
		pass
	
	@abstractmethod
	def TestConnection(self) -> tuple[bool, str]:
		return False, "Not Implemented"


@EmailHandler.register
class SMTPHandler (EmailHandler):
	server = ""
	port = 0
	username = ""
	password = ""
	security = ""
	config_file_path: str
	config: ConfigParser
	system: SMTP
	connected: bool = False
	
	def __init__(self, configFilePath: str) -> None:
		self.config = ConfigParser()
		self.config.read(configFilePath)
		self.username = self.config['DEFAULT']['Email']
		self.password = self.config['DEFAULT']['Password']
		self.server = self.config['DEFAULT']['SMTPServer']
		self.port = int(self.config['DEFAULT']['SMTPPort'])
		self.security = self.config['DEFAULT']['SMTPSecurity']

	def __del__(self) -> None:
		self.connected = False
		self.system.quit()
		del(self.system)
		
	def SendEmail(self, destination: str, content: str,
		text_content: str) -> list[str]:
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
		return msg.as_string().splitlines()

	def Connect(self) -> None:
		# Setup the SMTP system.
		self.system = SMTP(host=self.server, port=self.port)
		if self.security == 'TLS' and self.port != 25:
			self.system.starttls()
		self.system.login(self.username, self.password)
		self.connected = True

	def TestConnection(self) -> tuple[bool, str]:
		try:
			with SMTP(host=self.server, port=self.port,
				timeout=10) as smtp:
				if self.security == 'TLS' and self.port != 25:
					self.system.starttls()
				self.system.login(self.username, self.password)
				smtp.noop()

		except SMTPConnectError as error:
			return False, f"{error.errno}: {error.strerror}\n" \
				f"{error.smtp_code}: {error.smtp_error}"

		except SMTPException as error:
			return False, f"{error.errno}: {error.strerror}"
			
		return True, "OK"


@EmailHandler.register
class TXTHandler (EmailHandler):
	config: ConfigParser
	username: str
	config_file_path: str
	
	def __init__(self, configFilePath: str = "") -> None:
		self.config = ConfigParser()
		if configFilePath:
			self.config_file_path = configFilePath
			self.config.read(configFilePath)
			self.username = self.config['DEFAULT']['Email']
		else:
			self.username = "Facilitator@pollyanna.com"
	
	def __del__(self) -> None:
		pass

	def Connect(self) -> None:
		pass

	def TestConnection(self) -> tuple[bool, str]:
		return True, "OK"

	def SendEmail(self, destination: str, content: str,
		text_content: str) -> list[str]:
		fileName = sub("@.*", "", destination)
		fileName += ".email.txt"
		outputDir = expanduser('~/OutputMessages')
		if not isdir(outputDir):
			mkdir(outputDir)
		fileName = join(outputDir, fileName)
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
	email_handler: EmailHandler
	
	def __init__(self, recipient: str, content: str, text_content: str,
		handler: Optional[EmailHandler] = None):
		self.Recipient = recipient
		self.EmailContent = content
		self.EmailTextContent = text_content
		if handler is None:
			self.email_handler = SMTPHandler("creds.conf")
		else:
			self.email_handler = handler
			
	def __str__(self):
		return f"To: {self.Recipient}\n{self.EmailTextContent}"
	
	def SendEmail(self):
		return self.email_handler.SendEmail(self.Recipient,
		self.EmailContent, self.EmailTextContent)
