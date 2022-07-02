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

### EmailHandler.\_\_init\_\_(self, configFilePath: str) -> None ###

### EmailHandler.\_\_del\_\_(self) -> None ###

### EmailHandler.SendEmail(self, destination: str, content: str, text_content: str) -> list\[str\] ###

### EmailHandler.Connect(self) -> None ###

### EmailHandler.TestConnection(self) -> tuple\[bool, str\] ###

## SMTPHandler class ##

### SMTPHandler Properties ###

### SMTPHandler.\_\_init\_\_(self, configFilePath: str) -> None ###

### SMTPHandler.\_\_del\_\_(self) -> None ###

### SMTPHandler.SendEmail(self, destination: str, content: str, text_content: str) -> list\[str\] ###

### SMTPHandler.Connect(self) -> None ###

### SMTPHandler.TestConnection(self) -> tuple\[bool, str\] ###

## TXTHandler class ##

### TXTHandler Properties ###

### TXTHandler.\_\_init\_\_(self, configFilePath: str = "") -> None ###

### TXTHandler.\_\_del\_\_(self) -> None ###

### TXTHandler.Connect(self) -> None ###

### TXTHandler.TestConnection(self) -> bool ###

### TXTHandler.SendEmail(self, destination: str, content: str, text_content: str) -> list\[str\] ###

## Email class ##

### Email Properties ###

### Email.\_\_init\_\_(self, recipient: str, content: str, text_content: str, handler=None) -> None ###

### Email.\_\_str\_\_(self) -> str ###

### Email.SendEmail(self) -> None ###
