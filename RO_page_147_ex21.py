#RO_page_147_ex21

from random import*
x = 0
i = 0
while not abs(x) == 20:
    
    d = randint(1,2)
    i = i + 1
    if d == 1:
        x = x + 1
    elif d == 2:
        x = x - 1
print(x)
print(i, "intents")