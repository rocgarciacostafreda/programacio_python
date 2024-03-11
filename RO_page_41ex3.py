#RO_page_41ex3

n = int(input("n = "))
numero = 1
anterior = 0
suma = 0
x = 1
for x in range (1, n + 1, 1):
    seguent = anterior + numero
    anterior = numero
    numero = seguent
    suma = suma + anterior
print ("Total = ", suma)