# Person.py File Notes #

## Summary ##

Person.py contains both classes pertaining to the Pollyanna game itself: [`Person`](#person-class) and [`PollyannaGroup`](#pollyannagroup-class). These classes are used to initialize the Pollyanna pairings from a csv file containing information about each participant.

## Imports ##

This module imports several standard as well as external libraries:

### Standard Library ###

`csv`: `DictReader`

`random`: `choice`

`typing`: `Union`

## try_int(string: Union[str, bytes, bytearray], base: int = 10) -> Union[int, bool] ##

This allows one to attempt to parse a string into an int without building a try/except/finally block around it. If the string is able to be treated as an int, then it returns the int. It's meant to be used in this specific context:

```python
temp = try_int(input("Please enter a number: "))
some_int = temp if temp is not False else 0
```

It allows you to specify a default should the input not parse while avoiding cumbersome try/except statements.

## Person class ##

This class represents a person participating in the Pollyanna. It has a method that allows it to pick a mate randomly from the provided list while excluding the people who should not be picked for that person (self, spouse, etc).

### Person Properties ###

- `Name: str = ""`
- `FullName: str = ""`
- `EmailAddress: str = ""`
- `AmazonLink: str = ""`
- `IDNumber: int = 0`
- `Spouse: int = 0`
- `AlwaysGets: int = 0`
- `GiftsTo: 'Person'`

### Person.\_\_init\_\_(self, csvLine: dict) ###

This is the constructor for the `Person` class. It takes in a `dict[str, str]` of names and values from the CSV file. It has expectations for the names:

```python
csvLine.keys() == ['Name', 'Full Name', 'Email Address', 'Amazon Wishlist', 'ID', 'Spouse', 'I ALWAYS Get']
# True
```

The `dict[str, str]` is what is provided by [`DictReader`][csvLib-dictreader] when the reader reads in the file-handle on construction and then is iterated upon with a for-loop. This process happens in the `PollyannaGroup` constructor. Person then reads the keys listed above to fill in the property values except for "GiftsTo". `"ID"`, `"Spouse"`, and `"AlwaysGet"` are all converted to int from the dict. In the case of the latter two, they also default to 0 if they cannot be converted.

### Person.\_\_str\_\_(self) -> str ###

Returns a string representing some of the data in the Person class. There is some commented code that prints additional information but this is only used for debugging purposes.

### Person.mate(self, available: List) -> Person ###

The `mate` method takes in a list of available people to connect to for gifting. It produces a copy of the list and then removes this person instance's `Spouse`, `AlwaysGets`, and itself (`self.IDNumber`) by iterating through the list and checking if that person's ID is in the list of IDs to remove. It then checks if the resulting list is empty and if so returns `None`. Otherwise it uses the `random.choice()` function to pick from the remaining entries and assigns that to this person's `GiftsTo` property. Finally it returns the pick in case it is needed by the caller.

## PollyannaGroup class ##

This class pretends to be a Dictionary/Array that contains all of the [`Person`](#Person-class) objects which it generates from a [CSV file](https://github.com/GinoMan/PyPollyanna/blob/master/docs/data.md).

### PollyannaGroup Properties ###

- `people: list[Person]`

### PollyannaGroup.\_\_init\_\_(self, filename: str) ###

### PollyannaGroup.\_\_getitem\_\_(self, key: str | int) -> Person ###

### PollyannaGroup.\_\_str\_\_(self) -> str ###

### PollyannaGroup.\_\_iter\_\_(self) -> Person ###

### PollyannaGroup.\_\_len\_\_(self) -> int ###

### PollyannaGroup.shuffle(self) -> None ###

[csvlib]: https://docs.python.org/3.9/library/csv.html
[csvlib-dictreader]: https://docs.python.org/3.9/library/csv.html#csv.DictReader