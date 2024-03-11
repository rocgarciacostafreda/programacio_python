#RO_page_110_suma_quadrats

n = int(input("n = "))
suma = 0

for i in range(1, n+1):
    c = i**2
    suma = suma + c
print("La suma es", suma)