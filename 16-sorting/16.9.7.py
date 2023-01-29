"""
Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, 
top_three.
"""


import itertools
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

def return_values(k):
    return medals[k]


sorted_medals = (sorted(medals.keys(), key=return_values, reverse=True))
top_three = sorted_medals[:3]
print(top_three)