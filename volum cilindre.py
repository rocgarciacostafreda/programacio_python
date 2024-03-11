#PO_Àrea i volum cilindre
import math # llibreria de python

r = float(input("r = "))
h = float(input("h = "))
pi = 3.1416

s = (2*(pi*r**2)+2*pi*r*h)
v = (pi*r**2)*h

print ("s =", s)
print ("v =", v)