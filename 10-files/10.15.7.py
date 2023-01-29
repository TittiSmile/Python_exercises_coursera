"""
Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

"""

fileref = open("school_prompt.txt", "r")
beginning_chars = ""
reading = fileref.readline()
for i in reading[:30]:
    beginning_chars+=i
print(beginning_chars)
fileref.close()
