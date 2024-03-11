#RO_page_83_ex4

from math import*

numero = int(input("numero = "))

x = numero//100
resta = numero%100
y = resta//10
z = resta%10

resultat = x + (y * 10) + (z * 100)

print(resultat)