# Templates.py File Notes #

[![Author - Gino Vincenzini](https://raw.githubusercontent.com/GinoMan/PyPollyanna/master/docs/images/Author-Gino%20Vincenzini-brightgreen-badge.png)](https://ginovincenzini.com/)

## Summary ##

## Imports ##

This module imports several standard as well as external libraries:

### Standard Library ###

[`datetime`][datetime]: [`date`][datetime-date], [`timedelta`][datetime-timedelta]

### Packages ###

[`jinja2`][jinja2]: [`FileSystemLoader`][jinja2-FileSystemLoader], [`Environment`][jinja2-Environment], [`Template`][jinja2-Template]

### Custom Classes ###

[`Person`][Person]: [`Person`][Person-class]

## ContestSettings class ##

### ContestSettings Properties ###

### ContestSettings.\_\_init\_\_(self, facilitator: str, prize: str = "Bragging Rights", contest: bool = True) -> None ###

## EmailTemplate class ##

### EmailTemplate Properties ###

### EmailTemplate.\_\_init\_\_(self, templateDirectory: str, filename: str, settings: ContestSettings, html: bool = True) -> None ###

### EmailTemplate.render_for_person(self, person: Person) -> str ###

### EmailTemplate.render_and_assign(self, recipient: str, assignedName: str, assignedNameFull: str, amazonWishList: str) -> str ###

### EmailTemplate.render(self) -> str ###

### EmailTemplate.set_values(self, recipient: str, assignedName: str, assignedNameFull: str, amazonWishList: str) -> None ###

[abc]: https://docs.python.org/3.9/library/abc.html
[abc-abcmeta]: https://docs.python.org/3.9/library/abc.html#abc.ABCMeta
[abc-abstractmethod]: https://docs.python.org/3.9/library/abc.html#abc.abstractmethod

[argparse]: https://docs.python.org/3.9/library/argparse.html
[argparse-ArgumentParser]: https://docs.python.org/3.9/library/argparse.html#argparse.ArgumentParser
[argparse-Namespace]: https://docs.python.org/3.9/library/argparse.html#the-namespace-object
[argparse-RawTextHelpFormatter]: https://docs.python.org/3.9/library/argparse.html#formatter-class

[configparser]: https://docs.python.org/3.9/library/configparser.html
[configparser-ConfigParser]: https://docs.python.org/3.9/library/configparser.html#configparser-objects

[csvlib]: https://docs.python.org/3.9/library/csv.html
[csvlib-dictreader]: https://docs.python.org/3.9/library/csv.html#csv.DictReader

[datetime]: https://docs.python.org/3.9/library/datetime.html
[datetime-datetime]: https://docs.python.org/3.9/library/datetime.html#datetime-objects
[datetime-date]: https://docs.python.org/3.9/library/datetime.html#date-objects
[datetime-timedelta]: https://docs.python.org/3.9/library/datetime.html#timedelta-objects

[email-mime-multipart]: https://docs.python.org/3.9/library/email.mime.html#email.mime.multipart.MIMEMultipart

[email-mime-text]: https://docs.python.org/3.9/library/email.mime.html#email.mime.text.MIMEText

[os]: https://docs.python.org/3.9/library/os.html
[os-system]: https://docs.python.org/3.9/library/os.html#os.system
[os-get_terminal_size]: https://docs.python.org/3.9/library/os.html#os.get_terminal_size
[os-mkdir]: https://docs.python.org/3.9/library/os.html#os.mkdir

[os-path]: https://docs.python.org/3.9/library/os.path.html
[os-path-expanduser]: https://docs.python.org/3.9/library/os.path.html#os.path.expanduser
[os-path-isdir]: https://docs.python.org/3.9/library/os.path.html#os.path.isdir
[os-path-join]: https://docs.python.org/3.9/library/os.path.html#os.path.join

[pathlib]: https://docs.python.org/3.9/library/pathlib.html
[pathlib-Path]: https://docs.python.org/3.9/library/pathlib.html#pathlib.Path

[platform]: https://docs.python.org/3.9/library/platform.html
[platform-system]: https://docs.python.org/3.9/library/platform.html#platform.system

[random]: https://docs.python.org/3.9/library/random.html
[random-choice]: https://docs.python.org/3.9/library/random.html#random.choice

[re]: https://docs.python.org/3.9/library/re.html
[re-sub]: https://docs.python.org/3.9/library/re.html#re.sub

[smtplib]: https://docs.python.org/3.9/library/smtplib.html
[smtplib-SMTP]: https://docs.python.org/3.9/library/smtplib.html#smtplib.SMTP
[smtplib-SMTPConnectError]: https://docs.python.org/3.9/library/smtplib.html#smtplib.SMTPConnectError
[smtplib-SMTPException]: https://docs.python.org/3.9/library/smtplib.html#smtplib.SMTPException

[tempfile]: https://docs.python.org/3.9/library/tempfile.html
[tempfile-gettempdir]: https://docs.python.org/3.9/library/tempfile.html#tempfile.gettempdir

[typing]: https://docs.python.org/3.9/library/typing.html
[typing-Union]: https://docs.python.org/3.9/library/typing.html#typing.Union
[typing-Optional]: https://docs.python.org/3.9/library/typing.html#typing.Optional
[typing-iterable]: https://docs.python.org/3.9/library/typing.html#typing.Iterable

[colorama]: https://github.com/tartley/colorama
[colorama-back]: https://github.com/tartley/colorama#colored-output
[colorama-fore]: https://github.com/tartley/colorama#colored-output
[colorama-style]: https://github.com/tartley/colorama#colored-output
[colorama-deinit]: https://github.com/tartley/colorama#initialisation
[colorama-init]: https://github.com/tartley/colorama#initialisation

[jinja2]: https://jinja.palletsprojects.com/en/3.1.x/
[jinja2-FileSystemLoader]: https://jinja.palletsprojects.com/en/3.1.x/api/#jinja2.FileSystemLoader
[jinja2-Environment]: https://jinja.palletsprojects.com/en/3.1.x/api/#jinja2.Environment
[jinja2-Template]: https://jinja.palletsprojects.com/en/3.1.x/api/#jinja2.Template

[minify_html]: https://github.com/wilsonzlin/minify-html
[minify_html-minify]: https://docs.rs/minify-html/latest/minify_html/struct.Cfg.html

[progress-bar]: https://github.com/verigak/progress/
[progress-bar-IncrementalBar]: https://github.com/verigak/progress/#bars

[Main]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md
[Main-app_description]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md#app_description
[Main-reset_terminal_colors]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md#reset_terminal_colors---none
[Main-show_header]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md#show_headerprogram_name-str--the-pollyanna-lottery-system---none
[Main-display_example]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md#display_exampleperson-person-template-emailtemplate-txttemplate-emailtemplate---none
[Main-display_group]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md#display_groupgroup-pollyannagroup---none
[Main-display_associations]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md#display_associationsgroup-pollyannagroup---none
[Main-negative_answer]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md#negative_answerprompt_str-str-pos_answer-str--y---bool
[Main-parse_arguments]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md#parse_arguments---namespace
[Main-save_csv]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md#save_csvgroup-pollyannagroup---none
[Main-email_group]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md#email_groupgroup-pollyannagroup-template-emailtemplate-txttemplate-emailtemplate-is_test-bool---none
[Main-main]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md#main---none

[Person]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md
[try_int]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#try_intstring-unionstr-bytes-bytearray-base-int--10---unionint-bool

[Person-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#person-class
[Person-init]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#person__init__self-csvline-dictstr-str---none
[Person-str]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#person__str__self---str
[Person-mate]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#personmateself-available-listperson---unionperson-none

[PollyannaGroup-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#pollyannagroup-class
[PollyannaGroup-init]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#pollyannagroup__init__self-filename-str---none
[PollyannaGroup-getitem]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#pollyannagroup__getitem__self-key-unionstr-int---person
[PollyannaGroup-str]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#pollyannagroup__str__self---str
[PollyannaGroup-iter]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#pollyannagroup__iter__self---iteratorperson
[PollyannaGroup-len]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#pollyannagroup__len__self---int
[PollyannaGroup-shuffle]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#pollyannagroupshuffleself---none

[SendEmail]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md
[EmailHandler-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#emailhandler-class

[SMTPHandler-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#smtphandler-class
[SMTPHandler-init]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#smtphandler__init__self-configfilepath-str---none
[SMTPHandler-del]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#smtphandler__del__self---none
[SMTPHandler-SendEmail]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#smtphandlersendemailself-destination-str-content-str-text_content-str---liststr
[SMTPHandler-Connect]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#smtphandlerconnectself---none
[SMTPHandler-TestConnection]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#smtphandlertestconnectionself---tuplebool-str

[TXTHandler-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#txthandler-class
[TXTHandler-init]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#txthandler__init__self-configfilepath-str-----none
[TXTHandler-del]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#txthandler__del__self---none
[TXTHandler-SendEmail]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#txthandlerconnectself---none
[TXTHandler-Connect]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#txthandlertestconnectionself---bool
[TXTHandler-TestConnection]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#txthandlersendemailself-destination-str-content-str-text_content-str---liststr

[Email-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#email-class
[Email-init]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#email__init__self-recipient-str-content-str-text_content-str-handlernone---none
[Email-str]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#email__str__self---str
[Email-SendEmail]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#emailsendemailself---none

[Templates]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md
[ContestSettings-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md#contestsettings-class
[ContestSettings-init]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md#contestsettings__init__self-facilitator-str-prize-str--bragging-rights-contest-bool--true---none

[EmailTemplate-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md#emailtemplate-class
[EmailTemplate-init]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md#emailtemplate__init__self-templatedirectory-str-filename-str-settings-contestsettings-html-bool--true---none
[EmailTemplate-render_for_person]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md#emailtemplaterender_for_personself-person-person---str
[EmailTemplate-render_and_assign]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md#emailtemplaterender_and_assignself-recipient-str-assignedname-str-assignednamefull-str-amazonwishlist-str---str
[EmailTemplate-render]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md#emailtemplaterenderself---str
[EmailTemplate-set_values]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md#emailtemplateset_valuesself-recipient-str-assignedname-str-assignednamefull-str-amazonwishlist-str---none

[Data-csv]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/data.md

[Creds-conf]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/creds.md

[Tests]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/tests.md
