from Person import PollyannaGroup
from SendEmail import Email, TXTHandler
from Templates import EmailTemplate
from minify_html import minify

def main():
    group = PollyannaGroup('data.csv')
    group.shuffle()
    
    # Print the associations, and then allow the person to double check
    # If they're correct, save them in a text file in the user's dir
    # Then continue on, otherwise quit.
    
    template = EmailTemplate('Template', 'template.html')
    txtTemplate = EmailTemplate('Template', 'txttemplate.txt', False)
    
    # Grab the first person in the group, and open the template in a browser
    # Also print the text template. 
    
    for person in group:
        render = template.render_for_person(person)
        html = minify(render, minify_js=True, remove_processing_instructions=True)
        txt = txtTemplate.render_for_person(person)
        email = Email(person.EmailAddress, html, txt)
        email.SendEmail()

if (__name__ == "__main__"):
    main()