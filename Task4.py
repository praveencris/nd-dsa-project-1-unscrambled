"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_calls = set()
incomming_calls = set()
outgoing_texts = set()
incomming_texts = set()

for call in calls:
    outgoing_calls.add('{}'.format(call[0]))
    incomming_calls.add('{}'.format(call[1]))

for text in texts:
    outgoing_texts.add('{}'.format(text[0]))
    incomming_texts.add('{}'.format(text[1]))

# A-B All the elements of A which are not in B
# outgoing_calls - (incomming_calls U outgoing_texts U incomming_texts)
telemarketers = outgoing_calls.difference(
    incomming_calls.union(outgoing_texts.union(incomming_texts)))

print("These numbers could be telemarketers: ")
print(*list(telemarketers), sep='\n')
