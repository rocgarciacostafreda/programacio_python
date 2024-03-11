#RO_page_146_ex7

from math import*

n = int(input("n = "))
u = float(input("u = "))
v = float(input("v = "))

d = 0
d2 = 0
a = 0

while a < n:
    x = float(input("x = "))
    y = float(input("y = "))
    d = sqrt(pow(x,2) + pow(y,2))
    if d > d2:
        d2 = d
    a = a + 1
print("La distància més llarga és = ", d2)