"""
Below are a set of scores that students have received in the past semester. Write code to determine how many 
are 90 or above and assign that result to the value a_scores.
"""


scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
split_scores = scores.split(" ")
a_scores = 0
lst = []
for i in split_scores:
    lst.append(int(i))

for i in lst:
    if i >= 90:
        a_scores+=1
        
print(a_scores)