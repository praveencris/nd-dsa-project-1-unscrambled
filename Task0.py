"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from cgitb import text
import csv
with open('D:/Praveen/FSWebDev/Python/ND-DSA/Project-1/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('D:/Praveen/FSWebDev/Python/ND-DSA/Project-1/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


#Tasks0
first_text_record = texts[0]
print("First record of texts, {0} texts {1} at time {2}".format(first_text_record[0],first_text_record[1],first_text_record[2]))
first_call_record = calls[-1]
print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(first_call_record[0],first_call_record[1],first_call_record[2],first_call_record[3]))

#Query - Why, it was required to add fully qualified path?

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

