"""
Finally, generalize what you’ve done. Write a function that takes a string instead of a list as a parameter and returns a 
list of the five most frequent characters in the string.
"""


def five_most_frequent(string):
    d = {}
    for i in string:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1

    string = sorted(d, key=lambda x: d[x], reverse=True)

    return string[:5]

