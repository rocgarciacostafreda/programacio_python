#RO_page_83_ex5
from math import*

n = int(input("Nombre de dòllars = "))

dollar100 = n//100
dollar_restant = n%100

dollar50 = dollar_restant//50
dollar_restant_2 = dollar_restant%50

dollar20 = dollar_restant_2//20
dollar_restant_3 = dollar_restant_2%20

dollar10 = dollar_restant_3//10
dollar_restant_4 = dollar_restant_3%10

dollar5 = dollar_restant_4//5
dollar_restant_5 = dollar_restant_4%5

dollar1 = dollar_restant_5

print(dollar100, "Bitllets de 100$", dollar50, "Bitllets de 50$", dollar20, "Bitllets de 20$", dollar10, "Bitllets de 10$", dollar5, "Bitllets de 5$", dollar1, "Bitllets d'1$")