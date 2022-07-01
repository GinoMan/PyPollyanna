# SendEmail.py File Notes #

## Summary ##

## Imports ##

This module imports several standard as well as external libraries:

### Standard Library ###

`re`: `sub`

`os`: `mkdir`

`os.path`: `expanduser`, `isdir`, `join`

`configparser`: `ConfigParser`

`email.mime.multipart`: `MIMEMultipart`

`email.mime.text`: `MIMEText`

`smtplib`: `SMTP`, `SMTPConnectError`, `SMTPException`

`typing`: `Optional`

## EmailHandler class ##

### EmailHandler.\_\_init\_\_(self, configFilePath: str) ###

### EmailHandler.\_\_del\_\_(self) ###

### EmailHandler.SendEmail(self, destination: str, content: str, text_content: str) ###

### EmailHandler.Connect(self) ###

### EmailHandler.TestConnection(self) -> tuple[bool, str] ###

## SMTPHandler class ##

### SMTPHandler Properties ###

### SMTPHandler.\_\_init\_\_(self, configFilePath: str) ###

### SMTPHandler.\_\_del\_\_(self) ###

### SMTPHandler.SendEmail(self, destination: str, content: str, text_content: str) ###

### SMTPHandler.Connect(self) ###

### SMTPHandler.TestConnection(self) -> tuple[bool, str] ###

## TXTHandler class ##

### TXTHandler Properties ###

### TXTHandler.\_\_init\_\_(self, configFilePath: str = "") ###

### TXTHandler.\_\_del\_\_(self) ###

### TXTHandler.Connect(self) ###

### TXTHandler.TestConnection(self) ###

### TXTHandler.SendEmail(self, destination: str, content: str, text_content: str) ###

## Email class ##

### Email Properties ###

### Email.\_\_init\_\_(self, recipient: str, content: str, text_content: str, handler=None) ###

### Email.\_\_str\_\_(self) -> str ###

### Email.SendEmail(self) -> None ###
