#RO_page_95_ex5

from math import*

n = float(input("n = "))

if n%1 == 0:
    if n%7 == 0:
        print("És enter i divisible entre 7")
    else:
        print("És enter")
else:
    print("No és enter")