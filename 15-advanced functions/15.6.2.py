"""
Fill in the parameter list for g so that the invocations of g yield the return values specified
"""


def g(x,y=2,z=2):
    return 2*x + y + z
print(g(3))       # should output 10
print(g(3, 2))    # should output 8
print(g(3, 2, 1)) #should output 9


#g non aveva parametri inizialmente