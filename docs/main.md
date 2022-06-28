# main.py File Notes #

## Summary ##

This file contains the main method as well as some miscellaneous methods and a global that is used by the main function and its ancillary functions. Other files are reserved for particular classes within a domain and are documented in their respective markdown files.

## Imports ##

This program imports several standard as well as external libraries:

### Standard Library ###

`argparse`: `ArgumentParser`, `Namespace`, `RawTextHelpFormatter`

`datetime`: `datetime`

`os`: `path`, `system`, `get_terminal_size`

`pathlib`: `Path`

`random`: `choice`

`tempfile`: `gettempdir`

### Packages ###

`colorama`: `Back`, `Fore`, `Style`, `deinit`, `init`

`minify_html`: `minify` <- PyLance cannot find this function

`progress.bar`: `IncrementalBar`

### Custom Classes ###

[`Person`][Person]: [`Person`][Person-class], [`PollyannaGroup`][PollyannaGroup-class]

[`SendEmail`][sendemail]: [`Email`][email-class], [`TXTHandler`][txthandler-class]

[`Templates`][templates]: [`ContestSettings`][contestsettings-class], [`EmailTemplate`][emailtemplate-class]

## app_description ##

This variable contains a detailed description of the app used in the help text.

## reset_terminal_colors() -> None ##

This is a helper function that resets all of the color changes made to the terminal without breaking into a new line

## show_header(program_name: str = "THE POLLYANNA LOTTERY SYSTEM") -> None ##

This function shows the program header which is a red bar with Black/White text (depending on your terminal settings) welcoming the user to the program. It takes the `program_name` parameter which is used in the header. It can be changed at invocation but defaults to the above appended to "WELCOME TO ". The text is automatically centered in the terminal as well using [`get_terminal_size()`](https://docs.python.org/3.9/library/os.html#os.get_terminal_size).

## display_example(person: Person, template: EmailTemplate, txtTemplate: EmailTemplate) -> None ##

This function takes in a person, and both the text only and html templates, renders them, and then saves the resulting text to separate temporary files. It then opens both temporary files in the system's default browser and text editor. It currently supports the big three OS's: Windows, Mac, and Linux/UNIX (assuming that the Linux/UNIX system is running a desktop environment).

It works by calling the [`EmailTemplate.render_for_person()`](https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md#emailtemplaterender_for_personself-person-person---str) method of both templates against the [`Person`][person-class] object passed into the function, and then it asks the OS for a temporary directory, it saves both files into the temporary directory, finally it uses a dictionary to correspond the result of [`platform.system()`](https://docs.python.org/3.9/library/platform.html#platform.system) to the proper command to open the files and uses the [`os.system()`](https://docs.python.org/3.9/library/os.html#os.system) function to run the resulting command for both files.

The purpose is to allow the user to make sure the templates they may have altered in the templates folder render correctly and show the correct information in the right places and with the right linking.

## display_group(group: PollyannaGroup) -> None ##

This function only prints a listing of all of the assignment associations between participants in the [`PollyannaGroup`][pollyannagroup-class] object specified in the group parameter. The person on the left will buy and give a gift to the person on the right. Nobody should be missing from either side.

## display_associations(group: PollyannaGroup) -> None ##

This function displays the output from the `display_group()` function in a pretty format. It prints a line in red explaining that these are the associations, changes the color output to green text, and then prints the output of `display_group()`. Finally it resets the terminal colors using the `reset_terminal_colors()` function. 

## negative_answer(prompt_str: str, pos_answer:str = 'Y') -> bool ##

This function is meant to be used in code of the following sort:

```python
if negative_answer("Do you want to continue? "):
	quit()
```

Basically, if the user enters something other than some form of y\[es\], then the function returns `True`. Otherwise, it returns `False` and the conditional is skipped. It uses `input()` to query the user with the given prompt, and if they say anything but 'yes', the conditional executes. This was factored out of code that created several "answer" variables which were tested to see if they comported with anything but a positive answer (i.e. a negative answer, hence the name), to determine if the program should quit or not. But different cleanups were required at different points in the program so it didn't make sense to just have a "prompt to continue" function of some kind. Instead you can prompt for any yes or no question and if the answer is no, then execute the conditional. You can even use it for positive answers by putting `if not negative_answer(...)` instead.

The exact filtering the answer is subjected to is:

```python
not input(prompt).capitalize().strip().startswith(positive_answer or 'Y')
```

## parse_arguments() -> Namespace ##

This function creates an `ArgumentParser` instance with the `app_description` text as `description`, uses a formatter class to make sure the rendering is exact to how it's formatted in the `app_description` variable, and allows both `-` and `/` as command line switch prefixes. This means that `/t` and `-t` are the same. The available options are documented in the [README](https://github.com/GinoMan/PyPollyanna/blob/master/README.md#command-line-interface) file. It returns the `argparse.Namespace` object which holds the values of the correct types as values associated with keys named after the long argument without the dashes.

## save_csv(group: PollyannaGroup) -> None ##

In order to make sure that the associations are not lost, nor what the recipient's amazon wish list url is, a CSV file is generated with those values in the following format:

```csv
Full Name, Email Address, Assigned To, Assignee's Amazon Wishlist
```

The file is automatically saved with the name `{current_year} pollyanna assignments.csv` in the user's home directory. On Windows, this is `C:\\Users\\Username\\`; on Linux/UNIX/Darwin, this is `/home/username/`.

The file is then opened for writing, and the header is written. Finally it loops through every [`Person`][person-class] in the [`PollyannaGroup`][pollyannagroup-class], and writes formatted CSV data for them. Once finished, the context handler closes the file.

## email_group(group: PollyannaGroup, template: EmailTemplate, txtTemplate: EmailTemplate, is_test: bool) -> None ##

This function uses the group to determine the number of participants, and then shows a progress bar as it iterates through and emails the participants. It uses the number of participants (`len(group)`) to determine how many steps should be in that progress bar. It also shows a percentage and ETA. For each [`Person`][person-class] in the [`PollyannaGroup`][pollyannagroup-class], it generates a minified html rendering of the [`EmailTemplate`][EmailTemplate-class] for them as well as the text [`EmailTemplate`][emailtemplate-class] for them. It then checks if we're testing and if so, uses the [`TXTHandler`][TXTHandler-class] class to write the emails to a folder in the home folder. Otherwise it sends the emails directly using the same [`Email`][Email-class] class via an [`SMTPHandler`](https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#smtphandler-class) instance.

## main() -> None ##

This is the main function for the application. The function begins by initializing the terminal coloring and ends by de-initializing it. It saves the command line arguments and assigns the facilitator from the command line if one is specified. Then it opens up creates the [`PollyannaGroup`][Pollyannagroup-class] object from the `data.csv` file. Next it calls `show_header()` to display the banner before checking if the facilitator was specified, and if not, prompts for their full name. The program does not assume that the facilitator is part of the group, so it can be anyone. Next the facilitator and the prize and whether or not to have a gift-wrapping contest is put into a [`ContestSettings`][ContestSettings-class] object.

At this point we enter the second phase of the program which is randomly assigning people to each other using the [`PollyannaGroup.shuffle()`][pollyannagroup-class] method. Then the randomly decided associations are shown to the facilitator for final approval. If he approves, then the associations are saved into a CSV file and we move on to phase three.

The third and final phase is to generate the templates and if the user has not specified the quiet argument, to display examples of both the text only and HTML version of the emails in the default text editor and default browser respectively. The program then prompts the user to check both and make sure they have rendered correctly from the templates and reflect the choices they made in invoking the program and answering questions. If the user approves, then one final prompt is made as to whether or not to send out the emails. If the `--test` option is specified, then the emails will instead be written into a folder in the home directory. If the user says yes then either action is taken using a progress bar to track the action.

## if __name__ == '__main__' invocation ##

This invocation allows the `main.py` file to be referenced as a library. I wouldn't recommend it as it's not exactly built for that but it can be done if you want to borrow any of the functions in the code. Otherwise, it runs the `main()` function just like in a C-like language. It also includes a `try`/`finally` invocation to ensure that the terminal colors are reset and that colorama is uninitialized.

[person]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md
[person-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#person-class
[pollyannagroup-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/person.md#pollyannagroup-class
[SendEmail]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md
[TXTHandler-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#txthandler-class
[Email-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/sendemail.md#email-class
[Templates]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md
[ContestSettings-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md#contestsettings-class
[EmailTemplate-class]: https://github.com/GinoMan/PyPollyanna/blob/master/docs/templates.md#emailtemplate-class
