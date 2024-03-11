#rgarcia_3

def pagament1(preu):
    preu = 2.25
    preu_pagat = float(input("Preu pagat = "))
    while True:
        if preu < preu_pagat:
            canvi = preu_pagat - preu
            print("El teu canvi és de ", canvi, "€")
            break
        elif preu == preu_pagat:
            print("No hi ha canvi")
            break
        elif preu>preu_pagat:
            preu_a_pagar = preu - preu_pagat
            print("Falten ", preu_a_pagar, "€")
            preu_pagat_2 = float(input("Preu pagat = "))
            pagat_total = preu_pagat + preu_pagat_2
            if preu_total == preu:
                print("No hi ha canvi")
            elif preu_total > preu:
                canvi = preu_total - preu
                print("El teu canvi és de ", canvi, "€")
            elif preu_total < preu:
                print("No s'han insertat prous diners")
                print("Torna a intentar des del principi")
def pagament2(preu):
    preu = 1.75
    preu_pagat = float(input("Preu pagat = "))
    while True:
        if preu < preu_pagat:
            canvi = preu_pagat - preu
            print("El teu canvi és de ", canvi, "€")
            break
        elif preu == preu_pagat:
            print("No hi ha canvi")
            break
        elif preu>preu_pagat:
            preu_a_pagar = preu - preu_pagat
            print("Falten ", preu_a_pagar, "€")
            preu_pagat_2 = float(input("Preu pagat = "))
            pagat_total = preu_pagat + preu_pagat_2
            if preu_total == preu:
                print("No hi ha canvi")
            elif preu_total > preu:
                canvi = preu_total - preu
                print("El teu canvi és de ", canvi, "€")
            elif preu_total < preu:
                print("No s'han insertat prous diners")
                print("Torna a intentar des del principi")



gelat_avellana = 2,25
pastis_ametlla = 1,75

print("Tria el producte que vols")
print("")
print("1. Gelat d'avellana")
print("2. Pastís d'ametlla")
d = int(input("Tria el numero "))
if d == 1:
    preu = gelat_avellana
    pagament1(preu)
elif d == 2:
    preu = pastis_ametlla
    pagament2(preu)
else:
    print("Tria o el numero 1 o el numero 2")

