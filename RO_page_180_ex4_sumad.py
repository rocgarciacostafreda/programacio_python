#RO_page_180_ex4
from random import*
def sumad(n):
    for n in range(1,n+1):
        nombre_1 = n//100
        nombre_3 = n%10
        nombre_2 = (n//10)%10
        suma = nombre_1 + nombre_2 + nombre_3
    return suma

a = randint(1,101)
b = randint(1,101)
c = randint(1,101)
d = randint(1,101)
e = randint(1,101)
f = randint(1,101)

x1 = sumad(a)
x2 = sumad(b)
x3 = sumad(c)
x4 = sumad(d)
x5 = sumad(e)
x6 = sumad(f)

if x1 > x2 and x1  > x3 and x1 > x4 and x1 > x5 and x1 >x6:
    print("El nombre ",a, " té la suma de xifres més alta amb ",x1,)
elif x2 > x1 and x2  > x3 and x2 > x4 and x2 > x5 and x2 >x6:
    print("El nombre ",b, " té la suma de xifres més alta amb ",x2,)
elif x3 > x1 and x3  > x2 and x3 > x4 and x3 > x5 and x3 >x6:
    print("El nombre ",b, " té la suma de xifres més alta amb ",x2,)
elif x4 > x1 and x4  > x3 and x4 > x3 and x4 > x5 and x4 >x6:
    print("El nombre ",b, " té la suma de xifres més alta amb ",x2,)
elif x5 > x1 and x5  > x3 and x5 > x4 and x5 > x2 and x5 >x6:
    print("El nombre ",b, " té la suma de xifres més alta amb ",x2,)
elif x6 > x1 and x6  > x3 and x6 > x4 and x6 > x5 and x6 >x6:
    print("El nombre ",b, " té la suma de xifres més alta amb ",x2,)
else:
    print("Hi ha un empat entre nombres")