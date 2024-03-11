#RO_page32_cilindre

radi = float(input("Introdueix el radi = ",))
altura = float(input("Introdueix l'altura = ",))
pi = 3.1416

perímetre = (2 * pi * radi)
area = (pi * radi**2) + (2 * (perímetre * altura))
volum = (pi * radi**2) * altura

if altura > radi :
    print ("volum cilindre = ", volum, "cm3")
else : print ("area cilindre = ", area, "cm2")