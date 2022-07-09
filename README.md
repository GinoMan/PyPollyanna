# PyPollyanna #

[![Author - Gino Vincenzini](https://raw.githubusercontent.com/GinoMan/PyPollyanna/master/docs/images/Author-Gino%20Vincenzini-brightgreen-badge.png)](https://ginovincenzini.com/)

[![Lines of code](https://img.shields.io/tokei/lines/github/GinoMan/PyPollyanna?label=Total%20Lines&logo=github&logoColor=white&style=flat)](https://github.com/GinoMan/PyPollyanna)
[![GitHub License](https://img.shields.io/github/license/GinoMan/PyPollyanna?label=License&logo=creativecommons&logoColor=white&style=flat)](https://github.com/GinoMan/PyPollyanna/blob/master/LICENSE)
[![GitHub Downloads](https://img.shields.io/github/downloads/GinoMan/PyPollyanna/total?label=Github%20Downloads&logo=github)](https://github.com/GinoMan/PyPollyanna/releases)
[![Python 3.9+](https://img.shields.io/badge/Platform-Python_3.9-yellow?logo=python&logoColor=white&style=flat)](https://autohotkey.com)

Christmas is almost here and it's time to pick who's gifting to whom this Christmas. You can always get your group together and pick names out of a hat, but the problem is that sometimes people will pick their significant other \(so why have a Pollyanna for them\), or they pick themselves and have to draw again. So what to do? How about let the computer make sure that everything is fine?

That's where PyPollyanna comes in. I wrote it for my own family's yearly Pollyanna and we're currently using it this year. The program reads a list of participants from a CSV file, parses it into a list of people, and then pairs them up according to their parameters \(who their spouse is, who they feel like they always get, etc.\). It then creates an email to each of them and sends them a personalized email with their partner's name and amazon wish list.

## Requirements ##

### Runtime Requirements ###

- Python Version: 3.9+
- [colorama](https://pypi.org/project/colorama/): 0.4.4
- [Jinja2](https://pypi.org/project/Jinja2/): 3.0.3
- [minify_html](https://pypi.org/project/minify-html/): 0.7.0
- [progress](https://pypi.org/project/minify-html/): 1.6

### Development Requirements ###

- [check-requirements-txt](https://pypi.org/project/check-requirements-txt/): 1.0.2
- [flake8](https://pypi.org/project/flake8/): 4.0.1
- [pytest](https://pypi.org/project/pytest/): 6.2.5

### Recommended Environment ###

- [Visual Studio Code](https://code.visualstudio.com)
- [Python 3.9+](https://python.org)
- [Git 2.36.1+](https://git-scm.com/)

#### Recommended VSCode Plugins ####

- [Auto Close Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-close-tag)
- [Auto Rename Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag)
- [autoDocstring - Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
- [Better Jinja](https://marketplace.visualstudio.com/items?itemName=samuelcolvin.jinjahtml)
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
- [Comment Anchors](https://marketplace.visualstudio.com/items?itemName=ExodiusStudios.comment-anchors)
- [Importmagic](https://marketplace.visualstudio.com/items?itemName=codeavecjonathan.importmagic)
- [Ini for VSCode](https://marketplace.visualstudio.com/items?itemName=DavidWang.ini-for-vscode)
- [IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)
- [IntelliCode Completions](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode-completions)
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Code Documentation ##

1. [Main.PY](https://github.com/GinoMan/PyPollyanna/blob/master/docs/main.md)
1. [Person.PY](https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md)
1. [SendEmail.PY](https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md)
1. [Templates.PY](https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md)
1. [Tests](https://github.com/GinoMan/PyPollyanna/blob/master/docs/tests.md)
1. [Data.csv](https://github.com/GinoMan/PyPollyanna/blob/master/docs/data.md)
1. [Creds.conf](https://github.com/GinoMan/PyPollyanna/blob/master/docs/creds.md)

## Getting Started ##

1. You need your participants to register with you to fill out the CSV. I recommend sending them all a link to a google form with some questions \(Who do you always get, what's your amazon wish list, etc\). Then download the data and arrange it into a CSV file with the format described in the section "CSV".
1. You put the csv file in the project directory with the name "data.csv".
1. Create an ini file named "creds.conf" following the format in the section "Credential Config File" in the project directory.
1. Change the templates to include proper descriptions of your event and parameters.
1. Download the requirements from pip using requirements.txt; You must be on Python 3.9 or above to run the program.
1. And you're ready. Go ahead and run main.py in the terminal, and follow the prompts.

That's it! You've got a Pollyanna list and all of your participants have been emailed with whom they should buy a gift for.

## CSV File \(data.csv\) ##

The CSV File, data.csv, includes the information needed for the participants in the Pollyanna. The good news is that this can be adapted from a CSV export of a Google Form which is how I conducted the survey for the information.

The format for the file is a CSV meaning it's separated by commas and must contain a header. The header __MUST BE__:

`ID,Name,Full Name,I ALWAYS Get,Spouse,Email Address,Amazon Wishlist`

Otherwise, the program will not load it correctly. Each entry must be on a separate line. An example might look like:

```CSV
ID,Name,Full Name,I ALWAYS Get,Spouse,Email Address,Amazon Wishlist
1,Gino,Gino Contoso,-1,2,gino@contoso.com,https://www.amazon.com/wishlist
2,Cella,Marcela Contoso,-1,1,cella@contoso.com,https://www.amazon.com/wishlist
```

You can also open CSV files in Excel or OpenOffice/LibreOffice Calc. In that case it will be a table like this:

__ID__ | __Name__ | __Full Name__   | __I ALWAYS Get__ | __Spouse__ | __Email Address__ | __Amazon Wishlist__
-----: | -------- | --------------- | :--------------: | :--------: | ----------------- | ---------------------------------
1      | Gino     | Gino Contoso    | -1               | 2          | gino@contoso.com  | <https://www.amazon.com/wishlist>
2      | Cella    | Marcela Contoso | -1               | 1          | cella@contoso.com | <https://www.amazon.com/wishlist>

You will need a minimum of three unmarried people or two couples since built into the rules is the assumption that you cannot get your spouse for Pollyanna. This is because it is assumed that spouses will separately get each other gifts regardless the Pollyanna.

The fields which aren't obvious are explained below:

- __"ID"__ - This is a unique number, easiest just to start at 1 and increase from there
- __"I ALWAYS Get"__ - This is the ID of someone the person feels like they get every year or most years. The program will try to avoid assigning that person to them.
- __"Spouse"__ - This is the ID of the person's spouse. *Note: Both spouses should list the other partner.*

## Credential Config File \(creds.conf\) ##

The creds.conf file contains a listing of the information needed to make a secure connection to an email SMTP server to send out the notification emails to your participants so they know who has which participant for gift exchange, and what that person's amazon wishlist link is. The file is formatted like an INI file from windows config files and must contain the following section and keys (and your own settings rather than the contrived data below):

```ini
[DEFAULT]
Email = youremailaddress@gmail.com
Password = app_password_generated_by_gmail
SMTPServer = smtp.gmail.com
SMTPPort = 587
SMTPSecurity = TLS

[FACILITATOR]
Name = My Name
Event = Christmas 2022
```

The Email must be the email address that you use to log into the server. The Password is an app password generated by your email service or a regular password chosen by you for your email service. The SMTPServer, SMTPPort, and SMTPSecurity are values provided by your email service. SMTPSecurity can be one of the following:

- "TLS"
- "None"

The Facilitator section includes the name of the facilitator and the name of the event they are facilitating a Pollyanna for. It also specifies the prize/reward for winning the contest.

## Templates ##

There are two templates in the "Template" folder and these are used for the email that is sent to everyone. The two template.\[txt|html\].jinja files indicate the formatting for both the html and text only versions of the email. The master.jinja file indicates the text common to both as well as the variables used by its sections and the templates. 

### Master Template ###

The Master Template contains all of the common text between both types of emails. The defaults for the variables can be edited by the user and the information omitted but that's not the preferred way to handle changes to the information. Facilitator for examples can be specified on the command line, gained from the config file, or obtained interactively by the program.

- `reward` - The default email contains an invitation to participate in a voted gift wrapping contest. The participants are told the winner will receive this reward.
- `event_name` - The default email begins by announcing the beginning of the Pollyanna for a particular event \(Christmas, Hanukkah, Etc.\). This is where you name that event.
- `spending_limit` - A string describing the dollar amount total a gift or gifts should be to keep the gift giving fair.
- `facilitator` - The name of the person facilitating the event and thus sending the email.
- `due_date` - The cut-off after which people can buy gifts for each other. It's a last chance to edit your wishlist before the recipient of the list begins buying gifts for their assignment.

### HTML Template ###

The HTML template is for the rich-text version of the email. By default, it has some colors and images and the CSS for the email all in one file. It also has variables at the top that can be modified to contain more appropriate information. The variables not defined at the top of the template are used by the program to fill in for each individual recipient. They are:

- `background_color & background_color_2` - Hex code as a string for the colors used for the background of the email.
- `text_color` - color for the text to contrast against the backgrounds.

### Text Template ###

Some Email clients are unable to render HTML or the email service might not support HTML Emails. In that case, a plaintext version is sent along with the message so that those clients can correctly render the information for the user.

It includes all of the same variables as the HTML Template except the colors.

## Command Line Interface ##

Most people will just write the files themselves and run the program as is. But if you want to, you may specify some information on the command-line. The command is in the format:

main.py \[-h\] \[-t\] \[-f FACILITATOR\] \[-q\] \[-n | -p PRIZE\]

- __-h, --help__ - Shows the help message and exits
- __-t, --test__ - Do not send the final Emails, instead save them into a file
- __-f FACILITATOR, --facilitator FACILITATOR__ - The name of the person facilitating the Pollyanna
- __-q, --quiet__ - Determines whether or not to display sample emails
- __-n, --no-contest__ - Whether or not to host the gift-wrapping contest. Cannot use with `-p`
- __-p PRIZE, --prize PRIZE__ - The winner of the gift-wrapping contest receives this \(e.g. "A $100 Amazon Gift Card"\)

## Road Map ##

1. Finish Documentation of all code and type annotations
1. Add command-line options to specify config files
1. Prompt the user to enter people and generate the source CSV file manually if it's empty, missing, insufficient[^1], or improperly formatted[^2].
1. Allow the end user to specify additional variables to use for the templates
1. Automatically test email system before attempting to send emails.
1. Make more options specified on the command line.

[^1]: "insufficient" means that it doesn't reflect enough people.
[^2]: "improperly formatted* means that it doesn't have all of the columns it must have at minimum.
