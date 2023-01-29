"""

Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
"""
fileref = open("travel_plans.txt", "r")
first_chars = ""
reading = fileref.read()
for i in reading[:33]:
    first_chars+=i
fileref.close()


