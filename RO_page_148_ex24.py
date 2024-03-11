#RO_page_148_ex24

from random import*

n = int(input("n = "))
x = 0
suma = 0
while x < n:
    x = x + 1
    d = randint(1,6)
    if d == 1:
        suma = suma + 1
    elif d == 2 or d == 3 or d == 4 or d == 5:
        suma = suma - 2
    elif d == 6:
        suma = suma + 5
    print("tirada", x, "=", d)
    print("Suma = ", suma, "$")
print("Suma total = ", suma, "$")