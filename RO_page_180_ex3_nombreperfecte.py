#RO_page_180_ex3_nombreperfecte

def perfecto(n):
    suma = 0
    for i in range(1,n-1):
        if n%i == 0:
            suma = suma + i
            i = i + 1
        elif n%i != 0:
            i = i + 1
    return suma
for n in range(1,1001):
    suma = perfecto(n)
    if suma == n:
        print("El nombre ",n," és un nombre perfecte")
    else:
        print("El nombre ",n," no és un nombre perfecte")
