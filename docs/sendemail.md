# SendEmail.py File Notes #

## Summary ##

## Imports ##

This module imports several standard as well as external libraries:

### Standard Library ###

## EmailHandler class ##

### EmailHandler.\_\_init\_\_(self, configFilePath: str) ###

### EmailHandler.\_\_del\_\_(self) ###

### EmailHandler.SendEmail(self, destination: str, content: str, text_content: str) ###

### EmailHandler.Connect(self) ###

### EmailHandler.TestConnection(self) -> tuple[bool, str] ###

## SMTPHandler class ##

### SMTPHandler.\_\_init\_\_(self, configFilePath: str) ###

### SMTPHandler.\_\_del\_\_(self) ###

### SMTPHandler.SendEmail(self, destination: str, content: str, text_content: str) ###

### SMTPHandler.Connect(self) ###

### SMTPHandler.TestConnection(self) -> tuple[bool, str] ###

## TXTHandler class ##

### TXTHandler.\_\_init\_\_(self, configFilePath: str = "") ###

### TXTHandler.\_\_del\_\_(self) ###

### TXTHandler.TestConnection(self) ###

### TXTHandler.SendEmail(self, destination: str, content: str, text_content: str) ###

## Email class ##

### Email.\_\_init\_\_(self, recipient: str, content: str, text_content: str, handler=None) ###

