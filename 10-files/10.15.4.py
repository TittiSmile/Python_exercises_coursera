"""
The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
Find the total number of characters in the file and save to the variable num.

"""
fileref = open("travel_plans2.txt", "r")
reading = fileref.read()
num = 0
for i in reading:
    num+=1
print(num)
fileref.close()
