#RO_page_180_ex5_quadrat_nombre

def cuad(n):
    suma = 0
    for n in range(1,n+1):
        if n%2 == 0:
            suma = suma
        elif n%2 != 0:
            suma = suma + n
    print("La suma dels nombres imparells fins arribar a ",n, " és de ",suma)
    if (n**2) == suma:
        print("El nombre ",n, " elevat al quadrat és igual a la suma dels nombres imparells abans d'arribar al nombre ",n)
    elif (n**2) != suma:
        print("El nombre al quadrat i la suma dels nombres imparells no coincideixen")

n = int(input("n = "))
cuad(n)