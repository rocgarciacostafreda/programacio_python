#RO_page_97_ex20

c1 = float(input("c1 = "))
c2 = float(input("c2 = "))
c3 = float(input("c3 = "))

a1 = c1 * c2
a2 = c1 * c3
a3 = c2 * c3

if a1 > a2 and a1 > a3:
    print(a1, "m2")
elif a2 > a1 and a2 > a3:
    print(a2, "m2")
elif a3 > a1 and a2 < a3:
    print(a3, "m2")
elif a2 == a1 and a2 > a3:
    print(a2, "m2")
elif a3 == a1 and a2 < a3:
    print(a1, "m2")
elif a2 == a3 and a2 > a1:
    print(a2, "m2")
elif a2 == a1 and a1 == a3:
    print(a1, "m2")