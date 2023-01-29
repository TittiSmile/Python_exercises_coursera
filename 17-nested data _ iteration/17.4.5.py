"""
. Below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new 
list named b_strings.
"""


L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], 
     ['carrots', 'peas', 'cucumbers', 'green beans'], 
     ['root beer', 'smoothies', 'cranberry juice']]
b_strings = []
for lst in L:
    for fruits in lst:
        if "b" in fruits:
            b_strings.append(fruits)

#se NON ricordi che si può usare l'operatore in, puoi complicarti la vita così:

b_strings = []
for lst in L:
    for fruit in lst:
    	for letter in fruit:
    		if letter == "b":
            	b_strings.append(fruit)
            	break #metto break perchè le parole con due b dentro vengono aggiunte fue volte.