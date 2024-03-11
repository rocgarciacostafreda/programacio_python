#RO_page_97_ex19

j1 = int(input("j1 = "))
j2 = int(input("j2 = "))
j3 = int(input("j3 = "))

if j1 == 0 and j2 == 1 and j3 == 1:
    print("Continua")
elif j1 == 1 and j2 == 0 and j3 == 1:
    print("Continua")
elif j1 == 1 and j2 == 1 and j3 == 0:
    print("Continua")
elif j1 == 1 and j2 == 1 and j3 == 1:
    print("Continua")
elif j1 > 1 or j2 > 1 or j3 > 1:
    print("Error")
else:
    print("Eliminat")