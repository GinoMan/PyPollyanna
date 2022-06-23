from SendEmail import SMTPHandler, Email
from Templates import EmailTemplate
from Person import Person
from minify_html.minify_html import minify


def test_imports():
	emailSystem = SMTPHandler("creds.conf")
	assert isinstance(emailSystem, SMTPHandler)


def test_email_sending():
	message = "This is a test message. It is only a test!"
	email = Email("OpenMySourceCode@gmail.com", message, message)
	email.SendEmail()


def test_html_email_sending():
	message = """
	<html>
	<head></head>
	<body>
	<h1>HTML Test!</h1>
	</body>
	</html>
	"""
	txtmessage = "TXT Message"
	email = Email("OpenMySourceCode@gmail.com", message, txtmessage)
	email.SendEmail()


def test_HTML_templating():
	template = EmailTemplate("Template", 'template.html')
	txt = "TXT Message"
	rendered = template.render_and_assign("Gino", "Marcela",
		"Marcela Vincenzini", "https://www.amazon.com/")
	email = Email("OpenMySourceCode@gmail.com", rendered, txt)
	email.SendEmail()


def test_HTML_mini_templating():
	template = EmailTemplate("Template", 'template.html')
	txt = "TXT Message"
	rendered = template.render_and_assign("Gino", "Marcela", "Marcela Vincenzini",
		"https://www.amazon.com/")
	minified = minify(rendered, minify_js=True,
		remove_processing_instructions=True)
	email = Email("OpenMySourceCode@gmail.com", minified, txt)
	email.SendEmail()


def test_TXT_templating(capsys):
	template = EmailTemplate("Template", 'txttemplate.txt', False)
	txt = template.render_and_assign("Gino", "Marcela", "Marcela Vincenzini",
		"https://www.amazon.com/")
	email = Email("OpenMySourceCode@gmail.com", None, txt)
	email.SendEmail()
