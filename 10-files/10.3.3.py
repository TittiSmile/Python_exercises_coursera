"""
Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
"""


fileref = open("emotion_words2.txt", "r")
first_forty = ""
lines = fileref.readline()
for i in lines[:40]:
    first_forty+=i
print(first_forty)
fileref.close()

