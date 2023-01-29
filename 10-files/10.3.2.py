"""
Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
"""

fileref = open("travel_plans2.txt", "r")
reading = fileref.readlines()
num_lines=len(reading)
print(num_lines)
fileref.close()


