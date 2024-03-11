#RO_page_180_ex1_enters

def conteo(n):
    x = 0
    i = 1
    for i in range(1,n+1):
        if n%i == 0:
            print("El nombre ", i, " és divisor de ", n)
            x = x + 1
        else:
            i = i + 1
    return x

maxim = 0
for n in range (1,101):
    x = conteo(n)
    print("el numero de divisors de ", n , x)
    if x > maxim:
        maxim = x
        n = n
    print("El primer numero que té més divisors és ", maxim)
        