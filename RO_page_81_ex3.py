#RO_page_81_ex3

from math import*

base = float(input("Base = "))
altura = float(input("Altura = "))
profunditat = float(input("Profunditat = "))

area_bloc = (2*(base * altura)) + (2*(base * profunditat)) + (2*(profunditat * altura))
volum_bloc = base * altura * profunditat

print("Area = ", area_bloc, "m2")
print("Volum = ", volum_bloc, "m3")