#Write a function that removes all occurrences of a given letter from a string.


def remove_letter(theLetter, theString):
    # your code here
    s=theString
    for i in theString:
        if theLetter in theString:
            s = theString.replace(theLetter, "")
    return s




