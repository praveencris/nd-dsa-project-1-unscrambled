"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('D:/Praveen/FSWebDev/Python/ND-DSA/Project-1/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('D:/Praveen/FSWebDev/Python/ND-DSA/Project-1/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


telephone_duration = {}
for call in calls:
    for i in range(2):
        if telephone_duration.get(call[i]) == None:
             telephone_duration[call[i]] = int(call[3])
        else:
             telephone_duration[call[i]] += int(call[3])
            
result = max(telephone_duration.items(),key = lambda x: x[1])

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(result[0],result[1]))
