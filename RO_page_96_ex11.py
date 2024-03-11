#RO_page_96_ex11

from math import*
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
o1 = float(input("o1 = "))
o2 = float(input("o2 = "))

vectorposicio1 = sqrt((a1**2) + (a2**2))
vectorposicio2 = sqrt((o1**2) + (o2**2))

if vectorposicio1 > vectorposicio2:
    print("Punt 2")
elif vectorposicio1 < vectorposicio2:
    print("Punt 1")
elif vectorposicio1 == vectorposicio2:
    print("Punt 1 i punt 2")