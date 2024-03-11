#RO_page_95_ex2

from math import*

r = float(input("r = "))
h = float(input("h = "))

if h > r :
    volume = (pi * (r**2)) * h
    print(volume, "cm2")
else :
    print("Error")