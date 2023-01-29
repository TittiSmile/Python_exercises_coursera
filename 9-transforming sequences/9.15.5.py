"""
The module keyword determines if a string is a keyword. e.g. keyword.iskeyword(s) where s is a string will return either 
True or False, depending on whether or not the string is a Python keyword. Import the keyword module and test to see whether 
each of the words in list test are keywords. Save the respective answers in a list, keyword_test.


"""

import keyword
test = ["else", "integer", "except", "elif"]
keyword_test = []
for i in test:
    if keyword.iskeyword(i) == True:
        keyword_test.append(True)
    elif keyword.iskeyword(i) == False:
        keyword_test.append(False)
print(keyword_test)
