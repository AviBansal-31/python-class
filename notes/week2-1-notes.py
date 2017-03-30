x=123;y=123;
print("{} is {}: {}".format(x,y,x is y))
z=123
print("{} is {}: {}".format(x,z,x is z))
x= False
y= None
print("{} is not {}: {}".format(x,y,x is not y))
print("{} is (not{}: {}".format(x,y,x is y))

import timeit
#print(min(timeit.Timer('x is None', set up ="x=1").repeat))
