#RO_page_83_ex3

from math import*

numero_1 = int(input("numero 1 = "))
numero_2 = int(input("numero 2 = "))

x = numero_1//100
n_restante = numero_1%100
y = n_restante//10

a = numero_2//100
nrestante = numero_2%100
b = nrestante//10

resultat = y + b

print("Resultat = ", resultat)