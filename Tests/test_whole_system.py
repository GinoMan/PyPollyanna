from Person import PollyannaGroup
from SendEmail import Email, TXTHandler
from Templates import EmailTemplate
from minify_html import minify
from main import save_csv, display_example
from datetime import datetime
from os import path

def test_whole_system(capsys):
    group = PollyannaGroup('data.csv')
    group.shuffle()
    
    template = EmailTemplate('Template', 'template.html')
    txtTemplate = EmailTemplate('Template', 'txttemplate.txt', False)
    
    for person in group:
        handler = TXTHandler()
        render = template.render_for_person(person)
        html = minify(render, minify_js=True, remove_processing_instructions=True)
        txt = txtTemplate.render_for_person(person)
        email = Email('OpenMySourceCode@gmail.com', html, txt, handler)
        result = email.SendEmail()
        with capsys.disabled():
            print(result)
            
def test_email_system_by_sending_to_self(capsys):
    group = PollyannaGroup('data.csv')
    group.shuffle()
    
    template = EmailTemplate('Template', 'template.html')
    txtTemplate = EmailTemplate('Template', 'txttemplate.txt', False)
    
    for person in group:
        render = template.render_for_person(person)
        html = minify(render, minify_js=True, remove_processing_instructions=True)
        txt = txtTemplate.render_for_person(person)
        email = Email('OpenMySourceCode@gmail.com', html, txt)
        email.SendEmail()
        
def test_save_csv(capsys):
    group = PollyannaGroup('data.csv')
    group.shuffle()
    
    save_csv(group)
    
    with capsys.disabled():
        with open(path.expanduser(f'~/{datetime.now().year} pollyanna assignments.csv'), 'r') as csvFile:
            print(csvFile.read())
    
def test_display_example(capsys):
    group = PollyannaGroup('data.csv')
    group.shuffle()
    
    template = EmailTemplate('Template', 'template.html')
    txtTemplate = EmailTemplate('Template', 'txttemplate.txt', False)
    
    for person in group:
        display_example(person, template, txtTemplate)
        break
    
