#RO_page_182_ex21_nombres_triangulars

def triangular_for(n):
    suma = 0
    for n in range(1,n+1):
           suma = suma + n
    print("El nombre triangular de ",n, " és ",suma)

def triangular_while(n):
    suma = 0
    x = 1
    while x <= n:
        suma = suma + x
        x = x + 1
    print("El nombre triangular de ",n, " és ",suma)

def suma_triangulars(n):
    total = 0
    suma = 0
    for n in range(1,n+1):
        for n in range(1,n+1):
               suma = suma + n
    print("total = ", suma)

n_while = int(input("n_while = "))
triangular_while(n_while)
n_for = int(input("n_for = "))
triangular_for(n_for)
n_suma = int(input("n_suma = "))
suma_triangulars(n_suma)