#RO_Area_triangle.py
import math # llibreria de python

a = float(input("a = ")) # entrada de dades reals
b = float(input("b = "))
c = float(input("c = "))

t = (a+b+c)/2 # variables
s = math.sqrt(t*(t-a)*(t-b)*(t-c)) #càlculs
print("t =", t)
print("s =", s) # sortida de dades