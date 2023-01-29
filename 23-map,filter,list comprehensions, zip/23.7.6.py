"""
Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the 
variable opposites if they are both longer than 3 characters each.


"""

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

l3 = list(zip(l1,l2))

opposites = [i for i in l3 if len(i[0]) > 3] #in realtà funziona ma per puro caso :D i è la tupla. quindi se stampo len(i) mi darà 2 
print(opposites)
