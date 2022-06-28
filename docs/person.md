# Person.py File Notes #

## Summary ##

## Imports ##

This module imports several standard as well as external libraries:

### Standard Library ###

`csv`: `DictReader`

`random`: `choice`

`typing`: `List`

## Person class ##

### Person.\_\_init\_\_(self, csvLine: dict) ###

### Person.\_\_str\_\_(self) -> str ###

### Person.mate(self, available: List) -> Person ###

## PollyannaGroup class ##

### PollyannaGroup.\_\_init\_\_(self, filename: str) ###

### PollyannaGroup.\_\_getitem\_\_(self, key: str | int) -> Person ###

### PollyannaGroup.\_\_str\_\_(self) -> str ###

### PollyannaGroup.\_\_iter\_\_(self) -> Person ###

### PollyannaGroup.\_\_len\_\_(self) -> int ###

### PollyannaGroup.shuffle(self) -> None ###
