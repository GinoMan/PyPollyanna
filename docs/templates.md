# SendEmail.py File Notes #

## Summary ##

## Imports ##

This module imports several standard as well as external libraries:

### Standard Library ###

`datetime`: `date`, `timedelta`

### Packages ###

`jinja2`: `FileSystemLoader`, `Environment`, `Template`

### Custom Classes ###

`Person`: [`Person`](https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md)

## ContestSettings class ##

### ContestSettings.\_\_init\_\_(self, facilitator: str, prize: str = "Bragging Rights", contest: bool = True) ###

## EmailTemplate class ##

### EmailTemplate.\_\_init\_\_(self, templateDirectory: str, filename: str, settings: ContestSettings, html: bool = True) ###

### EmailTemplate.render_for_person(self, person: Person) -> str ###

### EmailTemplate.render_and_assign(self, recipient: str, assignedName: str, assignedNameFull: str, amazonWishList: str) -> str ###

### EmailTemplate.render(self) -> str ###

### EmailTemplate.set_values(self, recipient: str, assignedName: str, assignedNameFull: str, amazonWishList: str) ###
