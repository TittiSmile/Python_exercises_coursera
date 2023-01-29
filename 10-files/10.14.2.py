"""
The following sample file called studentdata.txt contains one line for each student in an imaginary class. The students name is 
the first thing on each line, followed by some exam scores. The number of scores might be different for each student.

joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89
Using the text file studentdata.txt write a program that prints out the names of students that have more than six quiz scores.
"""



# Hint: first see if you can write a program that just prints out the number of scores on each line
# Then, make it print the number only if the number is at least six
# Then, switch it to printing the name instead of the number
fileref = open("studentdata.txt", "r")
list_scores=[]
reading = fileref.readlines()
for i in reading:
    spl = i.split(" ")[1:]
    list_scores.append(spl)
#print(list_scores)
for i in list_scores:
    #a=i.strip("\n")
    print(i)
fileref.close()
#la soluzione sopra è IMPRECISA. ecco quella migliore:

f = open("studentdata.txt", "r")

for aline in f:
    items = aline.split()
    if len(items[1:]) > 6:
        print(items[0])

f.close()





