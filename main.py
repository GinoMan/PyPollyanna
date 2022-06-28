# PyPollyanna
# Written by Gino Vincenzini
# Copyright 2021 Gino Vincenzini. Licensed under MIT License

from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from datetime import datetime
from os import path, system, get_terminal_size
from pathlib import Path
from platform import system as platform_system
from random import choice
from tempfile import gettempdir

from colorama import Back, Fore, Style, deinit, init
from minify_html.minify_html import minify
from progress.bar import IncrementalBar

from Person import Person, PollyannaGroup
from SendEmail import Email, TXTHandler
from Templates import ContestSettings, EmailTemplate


app_description = r"""Christmas is almost here and it's time to pick who's \
gifting to whom this Christmas. You can always get your group together and \
pick names out of a hat, but the problem is that sometimes people will pick \
their significant other (so why have a Pollyanna for them), or they pick \
themselves and have to draw again. So what to do? How about let the computer \
make sure that everything is fine?

That's where PyPollyanna comes in. I wrote it for my own family's yearly \
Pollyanna and we're currently using it this year. The program reads a list of \
participants from a CSV file, parses it into a list of people, and then pairs \
them up according to their parameters (who their spouse is, who they feel \
like they always get, etc). It then creates an email to each of them and \
sends them a personalized email with their partner's name and amazon wish list.

By default, the email also mentions a gift-wrapping contest that we like to \
hold every year. If you don't desire to hold such a contest, you don't have \
to and can exclude it. If you do, you can specify a better reward than \
"bragging rights".
"""


def reset_terminal_colors():
	"""Resets the color effects in the terminal
	"""
	print(Style.RESET_ALL, end='')


def show_header(program_name: str = "THE POLLYANNA LOTTERY SYSTEM"):
	"""Shows the program Header banner.
	"""

	term_width = get_terminal_size().columns
	print(Back.RED + Fore.BLACK)
	print(' ' * term_width)
	print(f"WELCOME TO {program_name}!".center(term_width))
	print(' ' * term_width)
	reset_terminal_colors()


def display_example(person: Person, template: EmailTemplate,
		txtTemplate: EmailTemplate):
	"""Creates an example using the data for an Assigned Person

	Args:
		person (Person): The Assigned Person to use.
		template (EmailTemplate): The HTML Template to use for the email
		txtTemplate (EmailTemplate): The TXT only Template to use
	"""

	# create template with person
	render = template.render_for_person(person)
	txt = txtTemplate.render_for_person(person)
	temp = gettempdir()
	tmpHTMLFile = Path(temp) / "example.html"
	tmpTXTFile = Path(temp) / "example.txt"
	# show example on terminal of template
	with open(f"{tmpTXTFile}", 'w') as txtFile:
		txtFile.write(txt)
	# no need to output to the console anymore
	# print(Fore.MAGENTA + txt + Style.RESET_ALL)
	# open web browser of example for html
	with open(f"{tmpHTMLFile}", 'w') as htmlFile:
		htmlFile.write(render)

	# Make the command portable across operating systems
	command = {"Windows": "start", "Linux": "xdg-open", "Darwin": "open"}

	start_html: str = f"{command[platform_system()]} {tmpHTMLFile}"
	start_txt: str = f"{command[platform_system()]} {tmpTXTFile}"
	
	system(start_html)
	system(start_txt)


def display_group(group: PollyannaGroup):
	"""Prints a list of every member of the group and who they're assigned to

	Args:
		group (PollyannaGroup): The group of assigned people.
	"""

	for person in group:
		print(f"{person.FullName} -> {person.GiftsTo.FullName}")


def display_associations(group: PollyannaGroup):
	"""Display's the list of names and their associations for the user.
	with coloring and formatting.

	Args:
		group (PollyannaGroup): _description_
	"""
	print(Fore.RED + "The Associations are as follows:")
	print(Fore.GREEN, end='')
	display_group(group)
	reset_terminal_colors()


def negative_answer(prompt_str: str, pos_answer='Y') -> bool:
	"""Returns whether the user responded negatively to the prompt.
	It may seem confusing that the answer is in the negative, but the
	whole point is to allow the program or function to fail out if they
	do.

	Example:
		if negative_answer("Do you want to continue? "):
			quit()
	
	In the above example, true is returned unless they put in the default
	positive answer ('Y' or 'y'). The function normalizes their input to be
	capital and ignores anything after the first letter. It also strips
	the answer of leading and trailing whitespace. So Y, y, yes, Yes, YES
	are all acceptable positive answers to the prompt.

	Args:
		prompt_str (str): The prompt for the user to answer
		pos_answer (str, optional): What should return false. Defaults to 'Y'.

	Returns:
		bool: if the user put anything but pos_answer, return true
	"""
	return (not input(prompt_str).capitalize().strip().startswith(pos_answer))


def parse_arguments() -> Namespace:
	"""Parses Command Line Arguments

	Returns:
		argparse.Namespace: The object containing command line arg values
	"""

	arg_parser = ArgumentParser(description=app_description,
		formatter_class=RawTextHelpFormatter, prefix_chars='-/')
	arg_group = arg_parser.add_mutually_exclusive_group()

	arg_parser.add_argument("-t", "--test", action="store_true",
		help="do not send final emails, save instead")
	arg_parser.add_argument("-f", "--facilitator", type=str,
		help="The name of the facilitator")
	arg_parser.add_argument("-q", "--quiet", action="store_true",
		help="Determines whether or not to display sample emails")
	arg_group.add_argument("-n", "--no-contest", action="store_true",
		help="Whether or not there will be a gift-wrapping contest")
	arg_group.add_argument("-p", "--prize", type=str,
		help="The winner of the gift-wrapping contest receives this "
			"(e.g. \"A $100 Amazon Gift Card\").")

	return arg_parser.parse_args()


def save_csv(group: PollyannaGroup):
	"""Creates a full CSV File of the associations in the following format:
	Name | Full Name | Email Address | Amazon Link | Who Assigned To

	Args:
		group (PollyannaGroup): The Group imported from the CSV File
	"""

	# create a csv file of the results:
	# name, full-name, email-address, amazon-link, who-assigned-to
	filename = path.expanduser(f'~/{datetime.now().year} '
		'pollyanna assignments.csv')
	with open(filename, 'w') as csvFile:
		csvFile.write("Full Name, Email Address, Assigned, "
			"Assigned Amazon Link\n")
		for person in group:
			csvFile.write(f"{person.FullName}, {person.EmailAddress},"
			f"{person.GiftsTo.FullName}, {person.GiftsTo.AmazonLink}\n")


def email_group(group: PollyannaGroup, template: EmailTemplate,
		txtTemplate: EmailTemplate, is_test: bool):
	"""This emails the people on the list or generates text files
	for debugging containing the contents of both the txt and html
	templates with the values filled in. It also includes important
	Email related information like From, To, and Subject.

	Args:
		group (PollyannaGroup): The Group to email
		template (EmailTemplate): The HTML Template to use
		txtTemplate (EmailTemplate): The Text Template to use
		is_test (bool): whether to only generate files in testing
	"""

	number_of_participants = len(group)
	with IncrementalBar('Emailing Recipients', max=number_of_participants,
		suffix='%(percent).1f%% - %(eta)ds') as bar:
		for person in group:
			html = minify(template.render_for_person(person), minify_js=True,
				remove_processing_instructions=True)
			txt = txtTemplate.render_for_person(person)
			if is_test:
				email = Email(person.EmailAddress, html, txt, TXTHandler("creds.conf"))
			else:
				email = Email(person.EmailAddress, html, txt)
			email.SendEmail()
			bar.next()


def main():
	"""Main Method for application
	"""
	init()
	
	args = parse_arguments()
	facilitator = args.facilitator
	group = PollyannaGroup('data.csv')
	
	show_header()

	if args.facilitator is None:
		facilitator = input("Please Enter your full name here: ")
	
	contest = ContestSettings(facilitator, args.prize, not args.no_contest)
	group.shuffle()
	
	# Print the associations, and then allow the person to double check
	display_associations(group)

	if negative_answer(Fore.RED + "Is This Correct? [Y/N]: "):
		reset_terminal_colors()
		quit()
	# If they're correct, save them in a text file in the user's dir
	reset_terminal_colors()
	save_csv(group)
	
	template = EmailTemplate('Template', 'template.html.jinja', contest)
	txtTemplate = EmailTemplate('Template', 'text_template.txt.jinja',
		contest, False)
	
	if not args.quiet:
		display_example(choice(group.people), template, txtTemplate)
		# Prompt to continue or quit
		print("The text version of your email is open in your editor,"
			" and the html version in your browser.")
		if negative_answer("Are they correctly displayed? [Y/N]: "):
			quit()
	
	if args.test:
		print(Fore.RED + "The emails will now be generated and saved as text.")
	else:
		print("The emails will now be sent out using the provided settings.")

	if negative_answer("Are you sure? [Y/N]: "):
		reset_terminal_colors()
		quit()

	reset_terminal_colors()

	# some sort of email tester should go here to make sure there are no
	# issues with the email sending system.

	email_group(group, template, txtTemplate, args.test)
		
	deinit()


if (__name__ == "__main__"):
	try:
		main()
	finally:
		reset_terminal_colors()
		deinit()
