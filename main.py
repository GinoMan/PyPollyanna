from Person import PollyannaGroup
from SendEmail import Email, TXTHandler
from Templates import EmailTemplate
from minify_html import minify

def save_csv(group):
    # create a csv file of the results:
    # name, full-name, email-address, amazon-link, who-assigned-to
    pass

def display_example(person, template, txtTemplate):
    # create template with person
    # show example on terminal of template
    # open web browser of example for html
    pass

def main():
    group = PollyannaGroup('data.csv')
    group.shuffle()
    
    # Print the associations, and then allow the person to double check
    # If they're correct, save them in a text file in the user's dir
    # Then continue on, otherwise quit.
    
    
    template = EmailTemplate('Template', 'template.html')
    txtTemplate = EmailTemplate('Template', 'txttemplate.txt', False)
    
    for person in group:
        displayExample(person, template, txtTemplate)
        break
    
    # Prompt to continue or quit
    
    for person in group:
        render = template.render_for_person(person)
        html = minify(render, minify_js=True, remove_processing_instructions=True)
        txt = txtTemplate.render_for_person(person)
        email = Email(person.EmailAddress, html, txt)
        email.SendEmail()

if (__name__ == "__main__"):
    main()