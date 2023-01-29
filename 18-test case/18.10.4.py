"""

The class Student is supposed to accept two arguments in its constructor:
A name string

An optional integer representing the number of years the student has been at Michigan (default:1)

Every student has three instance variables:
self.name (set to the name provided)

self.years_UM (set to the number of years the student has been at Michigan)

self.knowledge (initialized to 0)

There are three methods:
.study() should increase self.knowledge by 1 and return None

.getKnowledge() should return the value of self.knowledge

.year_at_umich() should return the value of self.years_UM

There are one or more errors in the class. Use this space to write test cases to determine what errors there are. 
You will be using this information to answer the next set of multiple choice questions.
"""



class Student:
    name = ""
    years_UM = 1
    knowledge = 0
    def __init__(self, name, years_UM=1):
        self.name=name
    def study(self):
        self.knowledge+=1
        return None
    def getKnowledge(self):
        return self.knowledge
    def year_at_umich(self):
        return self.years_UM
    