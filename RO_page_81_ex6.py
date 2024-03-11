#RO_page_81_ex6

from math import*

examen = float(input("Nota examen(sobre 100) = "))
tasca_1 = float(input("Nota tasca 1(sobre 10) ="))
tasca_2 = float(input("Nota tasca 2(sobre 10) ="))
tasca_3 = float(input("Nota tasca 3(sobre 10) ="))
lliçons = float(input("Nota lliçó(sobre 10) ="))

examen = examen * 0.7
tasques = (((tasca_1 + tasca_2 + tasca_3) * 10) * 0.1)/3
lliçons = lliçons * 10 * 0.2

nota_final = examen + tasques + lliçons
print("Nota final = ", nota_final)