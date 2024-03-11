#RO_page_180_ex2_primers
from random import*
def primo(n):
    for i in range(2,n):
        if n%i == 0:
            print("El nombre",n,"no és nombre primer")
            break
        elif n%i != 0:
            i = i + 1
            if i == n-1:
                print("El nombre ", n, "és nombre primer")


a = randint(1,100)
b = randint(1,100)
print("El primer nombre és", a)
print("El segon nombre és", b)
print("")

n = a + b
print("La suma del nombre a i el nombre b és", n)

primo(n)

