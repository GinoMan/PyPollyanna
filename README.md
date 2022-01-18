# PyPollyanna #

Christmas is almost here and it's time to pick who's gifting to whom this Christmas. You can always get your group together and pick names out of a hat, but the problem is that you sometimes people will pick their significant other (so why have a pollyanna for them), or they pick themselves and have to draw again. So what to do? How about let the computer make sure that everything is fine?

That's where PyPollyanna comes in. I wrote it for my own family's yearly Pollyanna and we're currently using it this year. The program reads a list of participants from a CSV file, parses it into a list of people, and then pairs them up according to their parameters (who their spouse is, who they feel like they always get, etc). It then creates an email to each of them and sends them a personalized email with their partner's name and amazon wish list. 

## Getting Started ##

First, you need your participants to register with you to fill out the CSV. I recommend sending them all a link to a google form with some questions (Who do you always get, what's your amazon wish list, etc). Then download the data and arrange it into a CSV file with the format described in the section "CSV". 

Next, you put the csv file in the project directory with the name "data.csv". 

Third, create an ini file named "creds.conf" following the format in the section "Credential Config File".

Finally, download the requirements from pip using requirements.txt

And you're ready. Go ahead and run main.py in the terminal. 

That's it! You've got a pollyanna list and all of your participants have been emailed with whom they should buy a gift for. 

## CSV File ##

## Credential Config File ##

## Templates ##

