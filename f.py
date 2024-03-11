#RO_page32_kwfamilia

Kw_h = float(input("Introdueix Kw_h d'una família en un mes = ",))
preu = float(input("Introdueix el preu per Kw = ",))

cost = preu * Kw_h

if Kw_h > 700:
    cost = (preu * Kw_h) + (Kw_h - 700) *(1.05)

print ("cost = ", cost, "€")