"""
Write code that asks the user to enter a numeric score (0-100). In response, it should print out the score and corresponding 
letter grade, according to the table below.

Score   	Grade
>= 90    	A

[80-90)  	B

[70-80) 	C

[60-70)  	D

< 60   		F

The square and round brackets denote closed and open intervals. A closed interval includes the number, and open 
interval excludes it. So 79.99999 gets grade C , but 80 gets grade B.

"""

scores = [77.51, 92.86, 98.01, 69.71, 78.52, 59.69, 60.49, 85.04, 87.33, 91.04]
user_score = int(input("Digit score from 0 to 100: "))
grades = []
for i in scores:
    if i >= 90:
        grades.append("A")
    elif i>=80 and i <90 :
        grades.append("B")
    elif i >=70 and i<80:
        grades.append("C")
    elif i >=60 and i<70:
        grades.append("D")
    else:
        grades.append("F")
print(grades)
               
                   
