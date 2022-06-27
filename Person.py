# PyPollyanna Person Module
# Written by Gino Vincenzini
# Copyright 2021 Gino Vincenzini. Licensed under MIT License

from csv import DictReader
from random import choice
from typing import Union


class Person:
	Name: str = ""
	FullName: str = ""
	EmailAddress: str = ""
	AmazonLink: str = ""
	IDNumber: int = 0
	Spouse: int = 0
	AlwaysGets: int = 0
	GiftsTo: 'Person'
	
	def __init__(self, csvLine: dict):
		self.Name = csvLine["Name"]
		self.FullName = csvLine["Full Name"]
		self.EmailAddress = csvLine["Email Address"]
		self.AmazonLink = csvLine["Amazon Wishlist"]
		self.IDNumber = int(csvLine["ID"])
		self.Spouse = int(csvLine["Spouse"] or 0)
		self.AlwaysGets = int(csvLine["I ALWAYS Get"] or 0)
	
	def __str__(self):
		rep = (f"{self.IDNumber} | {self.FullName} ({self.Name})"
		f": Married To ID: {self.Spouse} - ")

		# Uncomment below for debugging purposes when debugging
		# rep += "\n\t"
		# if self.AlwaysGets > 0:
		#     rep += f"Always Gets ID: {self.AlwaysGets}\n\t"
		# else:
		#     rep += "Doesn't always get anyone\n\t"
		# rep += f"Email Address: {self.EmailAddress}\n\t"
		# rep += f"Amazon Wishlist: {self.AmazonLink}\n\t"

		if self.GiftsTo is not None:
			rep += f"Assigned To: {self.GiftsTo.Name}"
		else:
			rep += "Not Assigned To Anyone..."
		return rep
	
	def mate(self, available: list['Person']):
		locallyAvailable = available.copy()
		removeGroup = [self.Spouse, self.AlwaysGets, self.IDNumber]
		# remove spouse, and always get
		
		for person in locallyAvailable:
			if removeGroup.__contains__(person.IDNumber):
				locallyAvailable.remove(person)
		if len(locallyAvailable) <= 0:
			return None
		pick = choice(locallyAvailable)
		self.GiftsTo = pick
		return pick
		

class PollyannaGroup:
	people: list[Person]
	assignments: dict[Person, int]
	
	def __init__(self, fileName: str):
		self.people = []
		with open(fileName, newline='\n', encoding="UTF-8-sig") as csv_file:
			reader = DictReader(csv_file, delimiter=',',
			quotechar='"', skipinitialspace=True)
			for row in reader:
				self.people.append(Person(row))
	
	def __getitem__(self, key: Union[str, int]):
		for item in self.people:
			if isinstance(key, int) and item.IDNumber == key:
				return item
			elif isinstance(key, str) and (
				item.Name == key or item.FullName == key):
				return item
			else:
				continue
		raise KeyError(f"Nobody has an ID of {key}")
			
	def __str__(self):
		representation = ""
		for person in self.people:
			representation += f"{str(person)}\n"
		return representation
	
	def __iter__(self):
		return iter(self.people)
	
	def __len__(self):
		return len(self.people)
	
	def shuffle(self):
		while True:
			assignedAlready = []
			breakCondition = True
			for person in self.people:
				# determine possible people
				possible = self.people.copy()
				for item in assignedAlready:
					possible.remove(item)
				# use the mate function
				assignment = person.mate(possible)
				# if the assignment is none,
				# then there's nobody else they can have so we must trade
				if assignment is None:
					breakCondition = False
					break
				if assignment.IDNumber == person.IDNumber:
					breakCondition = False
					break
				if assignment.IDNumber == person.AlwaysGets:
					breakCondition = False
					break
				if assignment.IDNumber == person.Spouse:
					breakCondition = False
					break
				# use the result of the mate function to exclude from the assigned list
				assignedAlready.append(assignment)
			if breakCondition:
				break
