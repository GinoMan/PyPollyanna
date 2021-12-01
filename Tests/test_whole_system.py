from Person import PollyannaGroup
from SendEmail import Email, TXTHandler
from Templates import EmailTemplate
from minify_html import minify

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
        
