#RO_page_147_ex14

n = int(input("Nombre d'articles = "))
diners = float(input("Diners = "))
x = 0

while x < n:
    article = float(input("Article = "))
    x = x + 1
    if article <= diners:
        print("Aquest article es pot comprar")
        if article <= diners:
            nombre = diners//article
            print("Es poden comprar ", nombre, "articles")
    else:
        print("Aquest article no es pot comprar")