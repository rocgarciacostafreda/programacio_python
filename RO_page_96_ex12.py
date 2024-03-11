#RO_page_96_ex12

preu = float(input("preu = "))
articles = int(input("articles = "))

preu = preu * articles
if articles < 5 or articles == 5:
    print(preu, "$")
elif articles > 5 and articles < 10 or articles == 10:
    preu = preu * 0.95
    print(preu, "$")
elif articles > 10:
    preu = preu * 0.92
    print(preu, "$")