#RO_page_71_ex1
from math import*

radi = 5
area_cercle = pi * (radi)**2
perimetre_cercle = 2 * pi * radi
area_rectangle = perimetre_cercle * 4
area_cilindre = area_rectangle + (2 * area_cercle)
print("Area cilindre = ", area_cilindre, "m2")
volum_cilindre = area_cercle * 4
print("Volum cilindre = ", volum_cilindre, "m3")