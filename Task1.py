"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from __future__ import barry_as_FLUFL
import csv
with open('D:/Praveen/FSWebDev/Python/ND-DSA/Project-1/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('D:/Praveen/FSWebDev/Python/ND-DSA/Project-1/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Create a set of all phone numbers and calculate its size as sets never have any two elements as equal
telephone_numbers = set()
for text in texts:
    telephone_numbers.add('{}'.format(text[0]))
    telephone_numbers.add('{}'.format(text[1]))

for call in calls:
    telephone_numbers.add('{}'.format(call[0]))
    telephone_numbers.add('{}'.format(call[1]))

print("There are {} different telephone numbers in the records.".format(len(telephone_numbers)))