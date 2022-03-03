"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('D:/Praveen/FSWebDev/Python/ND-DSA/Project-1/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    print(texts)

with open('D:/Praveen/FSWebDev/Python/ND-DSA/Project-1/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)





"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

