#RO_page_180_ex9_dau
from random import*
def alfin(n):
    i = 1
    while True:
        d = randint(1,6)
        if n != d:
            i = i + 1
        elif n == d:
            print("El dau ha trigat",i,"vegades en treure el nombre",n)
            break
            


n = int(input("Tria el teu nombre "))
alfin(n)