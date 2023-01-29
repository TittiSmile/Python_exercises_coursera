"""
Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that only 
contains the strings from countries that begin with B.


"""
countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

def b_word(lst):
    for i in lst:
        if "b" in i or "B" in i:
            return True
    return False
    

b_countries = list(filter(b_word,countries)) 
#b_countries = list(filter(lambda word: "b" in word or "B" in word,countries)) #se non vuoi appoggiarti alla funzione
print(b_countries)