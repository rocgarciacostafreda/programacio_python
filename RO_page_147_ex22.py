#RO_page_147_ex22
from random import*

posicio1 = 0
posicio2 = 0
posicio3 = 0

x = 0
y = 0
z = 0

while posicio1 < 20:
    d = randint(1,4)
    x = x + 1
    if d == 1:
        posicio1 = posicio1
    elif d == 2:
        posicio1 = posicio1 + 0.5
    elif d == 3:
        posicio1 = posicio1 + 1
    elif d == 4:
        posicio1 = posicio1 - 0.5

while posicio2 < 20:
    e = randint(1,4)
    y = y + 1
    if e == 1:
        posicio2 = posicio2
    elif e == 2:
        posicio2 = posicio2 + 0.5
    elif e == 3:
        posicio2 = posicio2 + 1
    elif e == 4:
        posicio2 = posicio2 - 0.5

while posicio3 < 20:
    f = randint(1,4)
    z = z + 1
    if f == 1:
        posicio3 = posicio3
    elif f == 2:
        posicio3 = posicio3 + 0.5
    elif f == 3:
        posicio3 = posicio3 + 1
    elif f == 4:
        posicio3 = posicio3 - 0.5

print("La granota 1 ha arribat en ", x, "salts a la meta")
print("La granota 2 ha arribat en ", y, "salts a la meta")
print("La granota 3 ha arribat en ", z, "salts a la meta")

if x < y and x < z:
    print("Ha guanyat la granota 1")
elif y < x and y < z:
    print("Ha guanyat la granota 2")
elif z < x and y > z:
    print("Ha guanyat la granota 3")
elif x == y and x < z:
    print("Han guanyat la granota 1 i 2")
elif x == z and x < y:
    print("Han guanyat la granota 1 i 2")
elif z == y and x > z:
    print("Han guanyat la granota 1 i 2")
elif z == y and y == x:
    print("Han guanyat les tres granotes")