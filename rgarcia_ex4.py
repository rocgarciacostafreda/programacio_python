#rgarcia_challenge_ex4
from math import*
def segongrau ():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if (b**2)+ (-4 * a * c) < 0:
        print("La solució és imaginària")
    else:
        solucio1 = (-b+sqrt((b**2)-4 * a * c))/(2*a)
        solucio2 = (-b-sqrt((b**2)-4 * a * c))/(2*a)
        print("La solució 1 és igual a ",solucio1," la solució 2 és igual a ",solucio2)
x = segongrau()