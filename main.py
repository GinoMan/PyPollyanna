from datetime import datetime
from os import mkdir, path, system
from pathlib import Path
from tempfile import gettempdir
from colorama import init, deinit, Fore, Back, Style
from random import choice
from progress.bar import IncrementalBar

from minify_html.minify_html import minify

from Person import PollyannaGroup
from SendEmail import Email, TXTHandler
from Templates import EmailTemplate


def save_csv(group: PollyannaGroup):
	# create a csv file of the results:
	# name, full-name, email-address, amazon-link, who-assigned-to
	filename = path.expanduser(f'~/{datetime.now().year} '
		'pollyanna assignments.csv')
	with open(filename, 'w') as csvFile:
		csvFile.write("Full Name, Email Address, Assigned, Assigned Amazon Link\n")
		for person in group:
			csvFile.write(f"{person.FullName}, {person.EmailAddress},"
			f"{person.GiftsTo.FullName}, {person.GiftsTo.AmazonLink}\n")


def display_example(person, template, txtTemplate):
	# create template with person
	render = template.render_for_person(person)
	txt = txtTemplate.render_for_person(person)
	# show example on terminal of template
	print(Fore.MAGENTA + txt + Style.RESET_ALL)
	# open web browser of example for html
	temp = gettempdir()
	tempFile = Path(temp) / "example.html"
	with open(f"{tempFile}", 'w') as htmlFile:
		htmlFile.write(render)
	system(f"start {tempFile}")


def main():
	init()

	testing_mode = False
	
	print(Back.RED + Fore.BLACK)
	print("WELCOME TO THE POLLYANNA LOTTERY SYSTEM")
	print(Style.RESET_ALL)

	facilitator = input("Please Enter your full name here: ")
	
	group = PollyannaGroup('data.csv')
	group.shuffle()
	
	# Print the associations, and then allow the person to double check
	print("The Associations are as follows:")
	print(Fore.GREEN)
	for person in group:
		print(f"{person.FullName} -> {person.GiftsTo.FullName}")
	print(Style.RESET_ALL)
	answer = input(Fore.RED + "Is This Correct? [Y/N]: ")
	if not answer.capitalize().startswith('Y'):
		print(Style.RESET_ALL)
		quit()
	# If they're correct, save them in a text file in the user's dir
	print(Style.RESET_ALL)
	save_csv(group)
	
	template = EmailTemplate('Template', 'template.html.jinja', facilitator)
	txtTemplate = EmailTemplate('Template', 'txttemplate.txt.jinja',
		facilitator, False)
	
	display_example(choice(group.people), template, txtTemplate)
	
	# Prompt to continue or quit
	answer2 = input("Is this correctly displayed? [Y/N]: ")
	if not answer2.capitalize().startswith('Y'):
		quit()
	
	with IncrementalBar('Emailing Recipients', max=10,
		suffix='%(percent).1f%% - %(eta)ds') as bar:
		for person in group:
			render = template.render_for_person(person)
			html = minify(render, minify_js=True, remove_processing_instructions=True)
			txt = txtTemplate.render_for_person(person)
			if testing_mode:
				email = Email(person.EmailAddress, html, txt, TXTHandler())
			else:
				email = Email(person.EmailAddress, html, txt)
			email.SendEmail()
			bar.next()
		
	deinit()


if (__name__ == "__main__"):
	main()
