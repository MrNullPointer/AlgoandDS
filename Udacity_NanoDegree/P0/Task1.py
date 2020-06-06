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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

phone_number = []  # initializing an empty list

for line in texts:
    if line[0] not in phone_number:
        phone_number.append(line[0])
    if line[1] not in phone_number:
        phone_number.append(line[1])

for call in calls:
    if call[0] not in phone_number:
        phone_number.append(call[0])
    if call[1] not in phone_number:
        phone_number.append(call[1])

count = len(phone_number)

print("There are " + str(count) + " different telephone numbers in the records.")