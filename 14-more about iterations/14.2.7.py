"""
Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list 
called eve_nums.
"""
cont = 0
eve_nums = []
while cont <= 15:
    if cont % 2 == 0:
        eve_nums.append(cont)
    cont+=1