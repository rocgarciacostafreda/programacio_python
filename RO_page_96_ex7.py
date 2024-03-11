#RO_page_96_ex7

from math import*

t = float(input("t = "))
codi = float(input("codi = "))

if codi == 1:
    c = 5/9(t-32)
    print(c, "celcius")
elif codi == 2:
    f = 32 + 9*t/5
    print(f, "farenheit")
else:
    print("Error")