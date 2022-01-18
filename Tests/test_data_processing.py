from Person import PollyannaGroup, Person
import csv

def test_csv(capsys):
	with capsys.disabled():
		print('\n')
		with open('data.csv', newline='\n', encoding="UTF-8-sig") as csvfile:
			reader = csv.DictReader(csvfile, delimiter=',', quotechar='"', skipinitialspace = True)
			for row in reader:
				print(row)

def test_import_database(capsys):
	group = PollyannaGroup('data.csv')
	with capsys.disabled():
		print('\n')
		print(group)

def test_reference_person(capsys): # Success!
	group = PollyannaGroup('data.csv')
	with capsys.disabled():
		print("\n")
		print(group["Mario"])
		print(group["Gino"])
		print(group[7])
		
def test_shuffling(capsys):
	group = PollyannaGroup('data.csv')
	group.shuffle()
	with capsys.disabled():
		print("\n")
		print(group)

