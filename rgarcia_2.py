#rgarcia_2.py

x = int(input("x = "))

a = x%19
b = x%14
c = x%7
d = ((19 * a) + 24)%30
e = ((2 * b) + (4*c) + (6 * d) + 5)%7
f = 22 + d + e

if f < 31 and f > 0:
    print(f, "gener")
elif f >= 32 and f <= 59:
    f = f - 31
    print(f, "febrer")
elif f >= 60 and f <= 90:
    f = f - 31
    print(f, "març")
elif f >= 91 and f <= 120:
    f = f - 31 - 28
    print(f, "abril")
elif f >= 121 and f <= 151:
    f = f - 31 - 28 - 31
    print(f, "maig")
elif f >= 152 and f <= 181:
    f = f - 31 - 28 - 31 - 30
    print(f, "juny")