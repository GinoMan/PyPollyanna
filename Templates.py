from jinja2 import FileSystemLoader, Environment, Template
from Person import Person
from datetime import date, timedelta
import minify_html
import typing
import types


class EmailTemplate:
	recipient = ""
	assignedName = ""
	assignedNameFull = ""
	amazonWishList = ""
	filename = ""
	template_object: Template
	env: Environment
	rendering: str
	is_html: bool
	facilitator: str
	
	def __init__(self, templateDirectory, filename, facilitator, html=True):
		file_loader = FileSystemLoader(templateDirectory)
		env = Environment(loader=file_loader)
		if(html):
			env.trim_blocks = True
			env.lstrip_blocks = True
			# env.rstrip_blocks = True	# Doesn't exist?
		else:
			env.trim_blocks = False
			env.lstrip_blocks = False
			# env.rstrip_blocks = False	# Doesn't exist?
		self.filename = filename
		self.env = env
		self.is_html = html
		self.facilitator = facilitator
	
	# render
	def render_for_person(self, person: Person):
		return self.render_and_assign(person.Name, person.GiftsTo.Name,
		person.GiftsTo.FullName, person.GiftsTo.AmazonLink)
	
	def render_and_assign(self, recipient, assignedName, assignedNameFull,
		amazonWishList) -> str:
		self.set_values(recipient, assignedName, assignedNameFull, amazonWishList)
		return self.render()
		
	def render(self):
		self.template_object = self.env.get_template(self.filename)
		self.rendering = self.template_object.render(
			recipient=self.recipient,
			assignedName=self.assignedName,
			assignedNameFull=self.assignedNameFull,
			amazonWishList=self.amazonWishList,
			html=self.is_html,
			facilitator=self.facilitator,
			date=date,
			timedelta=timedelta)
		return self.rendering
		
	def set_values(self, recipient, assignedName,
		assignedNameFull, amazonWishList):
		self.recipient = recipient
		self.assignedName = assignedName
		self.assignedNameFull = assignedNameFull
		self.amazonWishList = amazonWishList
