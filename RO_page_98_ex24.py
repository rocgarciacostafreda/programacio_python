#RO_page_98_ex24
#materia a = 1 and materia b = 2 and materia ab = 3
e1 = int(input("e1 = "))
e2 = int(input("e2 = "))
e3 = int(input("e3 = "))

if e1 == 3 and e2 != 3 and e3 != 3:
    print(1)
elif e1 != 3 and e2 != 3 and e3 != 3:
    print(0)
elif e1 != 3 and e2 == 3 and e3 != 3:
    print(1)
elif e1 != 3 and e2 != 3 and e3 == 3:
    print(1)
elif e1 == 3 and e2 == 3 and e3 != 3:
    print(2)
elif e1 == 3 and e2 != 3 and e3 == 3:
    print(2)
elif e1 != 3 and e2 == 3 and e3 == 3:
    print(2)
elif e1 == 3 and e2 == 3 and e3 == 3:
    print(3)