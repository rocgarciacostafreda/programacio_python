#RO_page_95_ex1

from math import*

r = float(input("r = "))
h = float(input("h = "))

if h > r :
    volume = (pi * (r**2)) * h
    print(volume, "cm2")
else :
    perimetre = 2 * pi * r
    area = (2 * (pi * (r**2))) +(h * perimetre)
    print(area, "cm")