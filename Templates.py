from jinja2 import FileSystemLoader, Environment, Template
from Person import Person
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
	
	def __init__(self, templateDirectory, filename, html=True):
		file_loader = FileSystemLoader(templateDirectory)
		env = Environment(loader=file_loader)
		if(html):
			env.trim_blocks = True
			env.lstrip_blocks = True
			env.rstrip_blocks = True
		else:
			env.lstrip_blocks = False
			env.rstrip_blocks = False
			env.trim_blocks = False
		self.filename = filename
		self.env = env
	
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
			amazonWishList=self.amazonWishList)
		return self.rendering
		
	def set_values(self, recipient, assignedName, assignedNameFull, amazonWishList):
		self.recipient = recipient
		self.assignedName = assignedName
		self.assignedNameFull = assignedNameFull
		self.amazonWishList = amazonWishList