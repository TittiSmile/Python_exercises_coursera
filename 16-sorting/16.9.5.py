"""
Write code to switch the order of the winners list so that it is now A to Z by last name. Assign this list to the variable 
z_winners.
"""


winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners =  sorted(winners, key=lambda name: name.split()[-1])

#N.B. il [-1] è per chi ha anche il nome centrale. altrimenti andava bene pure solo [1]