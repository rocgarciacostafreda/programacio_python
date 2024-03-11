#RO_page_81_ex1

from math import*

radi = float(input("radi = "))
altura = float(input("altura = "))

area_cercle = pi * (radi ** 2)
perimetre = 2 * pi * radi
area_rectangle = altura * perimetre
area_cilindre = area_rectangle + (2 * area_cercle)
volum_cilindre = altura * area_cercle

print("Area del cilindre = ", area_cilindre)
print("Volum del cilindre = ", volum_cilindre)