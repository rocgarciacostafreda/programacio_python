#RO_page_71_ex4

from math import*
#aillar la k a l'equació de l'exercici
t = int(input("Temps en anys = "))
k = (50-2*e)/10

f = (k * t) + 2 * (e**(0.1*t))

print("Creixement de població =",f, "%")