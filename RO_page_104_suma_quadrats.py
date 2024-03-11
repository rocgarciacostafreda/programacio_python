#RO_page104_suma_quadrats

n = int(input("n = "))
x = 0
c = 1
suma = 0
while x < n:
    suma = suma + c**2
    x = x + 1
    c = c + 1
print("La suma es", suma)