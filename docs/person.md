# Person.py File Notes #

[![Author - Gino Vincenzini](https://raw.githubusercontent.com/GinoMan/PyPollyanna/master/docs/images/Author-Gino%20Vincenzini-brightgreen-badge.png)](https://ginovincenzini.com/)

## Summary ##

Person.py contains both classes pertaining to the Pollyanna game itself: [`Person`][person-class] and [`PollyannaGroup`][pollyannagroup-class]. These classes are used to initialize the Pollyanna pairings from a csv file containing information about each participant.

## Imports ##

This module imports several standard as well as external libraries:

### Standard Library ###

[`csv`][csvlib]: [`DictReader`][csvlib-dictreader]

[`random`][random]: [`choice`][random-choice]

[`typing`][typing]: [`Union`][typing-union]

## try_int(string: Union\[str, bytes, bytearray\], base: int = 10) -> Union\[int, bool\] ##

This allows one to attempt to parse a string into an int without building a try/except/finally block around it. If the string is able to be treated as an int, then it returns the int. It's meant to be used in this specific context:

```python
temp = try_int(input("Please enter a number: "))
some_int = temp if temp is not False else 0
```

It allows you to specify a default should the input not parse while avoiding cumbersome try/except statements.

## Person class ##

This class represents a person participating in the Pollyanna. It has a method that allows it to pick a mate randomly from the provided list while excluding the people who should not be picked for that person (self, spouse, etc).

### Person Properties ###

- `Name: str = ""`
- `FullName: str = ""`
- `EmailAddress: str = ""`
- `AmazonLink: str = ""`
- `IDNumber: int = 0`
- `Spouse: int = 0`
- `AlwaysGets: int = 0`
- `GiftsTo: 'Person'`

### Person.\_\_init\_\_(self, csvLine: dict\[str, str\]) -> None ###

This is the constructor for the `Person` class. It takes in a `dict[str, str]` of names and values from the CSV file. It has expectations for the names:

```python
csvLine.keys() == ['Name', 'Full Name', 'Email Address', 'Amazon Wishlist', 'ID', 'Spouse', 'I ALWAYS Get']
# True
```

The `dict[str, str]` is what is provided by [`DictReader`][csvLib-dictreader] when the reader reads in the file-handle on construction and then is iterated upon with a for-loop. This process happens in the `PollyannaGroup` constructor. Person then reads the keys listed above to fill in the property values except for "GiftsTo". `"ID"`, `"Spouse"`, and `"AlwaysGet"` are all converted to int from the dict. In the case of the latter two, they also default to 0 if they cannot be converted.

### Person.\_\_str\_\_(self) -> str ###

Returns a string representing some of the data in the Person class. There is some commented code that prints additional information but this is only used for debugging purposes.

### Person.mate(self, available: list\['Person'\]) -> Union['Person', None] ###

The `mate` method takes in a list of available people to connect to for gifting (i.e. those who haven't already been chosen). It produces a copy of the list and then removes this person instance's `Spouse`, `AlwaysGets`, and itself (`self.IDNumber`) by iterating through the list and checking if that person's ID is in the list of IDs to remove. It then checks if the resulting list is empty and if so returns `None`. Otherwise it uses the `random.choice()` function to pick from the remaining entries and assigns that to this person's `GiftsTo` property. Finally it returns the pick in case it is needed by the caller.

## PollyannaGroup class ##

This class pretends to be a Dictionary/Array that contains all of the [`Person`](#Person-class) objects which it generates from a [CSV file](https://github.com/GinoMan/PyPollyanna/blob/master/docs/data.md). It acts as a wrapper for a list object that has all of the ['Person'][person-class] objects generated and provides a shuffle method that assigns everyone to random other persons in the list. It's also iterable so it can be used in `for ... in ...` loops and list comprehensions. 

### PollyannaGroup Properties ###

- `people: list[Person]`

### PollyannaGroup.\_\_init\_\_(self, filename: str) -> None ###

This is the constructor for the PollyannaGroup class. It initializes `self.people` with an empty list. Then it opens the provided filename which is a CSV file and uses [`DictReader`][csvlib-dictreader] to create a ['Person'][person-class] object from each row in the CSV file and appending that person to the internal `self.people` list.

### PollyannaGroup.\_\_getitem\_\_(self, key: Union\[str, int\]) -> Person ###

This method allows for the use of square bracket syntax to look-up a Person object in the group. You can look up by ID (so a number) or by First or Full Name. 

Examples:

```python
group = PollyannaGroup("data.csv")

# Look up by ID Number:
someone = group[1]

# Look up by First Name:
someoneElse = group["Jackson"]

# look up by Full Name:
someoneMore = group["Exer Campbell"]  # Character from Jackson's Diary Web-comic
```

### PollyannaGroup.\_\_str\_\_(self) -> str ###

Converts the group to string listing each person in the group in the following format:

\[Number\] \| \[Full Name\] (\[First Name\]) Married To ID: \[Spouse.ID\] - Assigned to: \[GiftsTo.Name\]

of if they are not assigned:

\[Number\] \| \[Full Name\] (\[First Name\]) Married To ID: \[Spouse.ID\] - Not Assigned To Anyone...

Each entry is on its own line but is all in one string. 

### PollyannaGroup.\_\_iter\_\_(self) -> Iterable\[Person\] ###

Simply returns the iterator for the List of Persons contained in the class enabling use in iteration statements (usually for ... in ... loops).

### PollyannaGroup.\_\_len\_\_(self) -> int ###

Returns the number of entries in the group.

### PollyannaGroup.shuffle(self) -> None ###

Uses the "Person.Mate" method to randomly pair up the participants observing the rules of not getting yourself, your spouse, or the person you "always get". It loops infinitely until everyone is paired up. So the pairing is always guaranteed to succeed.

It works by creating an empty `"assignedAlready"` List to store all the picks that have been made (to prevent multiple persons getting the same person to get a gift for), and adding to that list every iteration every person who has been assigned. This outer loop repeats every time the inner `for` loop fails to assign everyone. It gets a copy of everyone, removes every object reference from that copy of the list everyone that has been assigned already, and then calls the `mate` method.

Then, it checks then if any of the rules are broken by the match: it couldn't assign anyone, it assigned themselves, it assigned the person they always get, or it assigns their spouse. If any of these are met, the `breakCondition` is set to `False`, and the for-loop is broken out of to restart the process from the beginning.

This resets the state and we try again. Since the references are re-assigned, only the two variables inside the while loop need to be reset.

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
[PollyannaGroup-iter]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#pollyannagroup__iter__self---iterableperson
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