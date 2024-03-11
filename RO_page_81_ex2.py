#RO_page_81_ex2

from math import*

v = float(input("Volum en litres = ",))
h = float(input("Altura en metres = ",))

v = v/1000

r = sqrt (v/(pi * h))
d = r * 2
print("Diametre = ", d)