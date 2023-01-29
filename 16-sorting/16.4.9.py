"""
Sort the following dictionary’s keys based on the value from highest to lowest. Assign the resulting value to the variable 
sorted_values.
"""


dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 
              'Grill': 2, 'Lights': 14}

def return_values(k):
    return dictionary[k]


sorted_values = (sorted(dictionary.keys(), key=return_values, reverse=True))


