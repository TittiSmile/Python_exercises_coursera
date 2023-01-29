"""
Fill in the left side of line 7 so that the following code runs without error
"""


def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

area,circ = circleInfo(10)	#ecco, qui associamo due variabili al metodo. 
                            #in questo modo ogni valore della tupla verrà assegnato ad una variabile
print("area is " + str(area))
print("circumference is " + str(circ))
