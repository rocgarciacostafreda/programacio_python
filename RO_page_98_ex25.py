#RO_page_98_ex25

kg = float(input("kg = "))

if kg < 3:
    preu = kg * 2.4
    print(preu, "$")
elif kg >= 3 and kg < 6:
    preu = kg * 2.3
    print(preu, "$")
elif kg >= 6 and kg <= 10:
    preu = kg * 2.1
    print(preu, "$")
elif kg > 10:
    preu = kg * 1.85
    print(preu, "$")