#RO_page_95_ex3

from math import*

altura = float(input("Altura = "))
amplada = float(input("Amplada = "))
profunditat = float(input("Profunditat = "))

diagonal1 = sqrt(altura**2 + amplada**2)
diagonal2 = sqrt(altura**2 + profunditat**2)
diagonal3 = sqrt(amplada**2 + profunditat**2)

if diagonal1 > diagonal2 and diagonal1 > diagonal3:
    print("Diagonal altura-amplada", diagonal1)
elif diagonal2 > diagonal1 and diagonal2 > diagonal3 :
    print("Diagonal altura-profunditat", diagonal2)
elif diagonal3 > diagonal1 and diagonal3 > diagonal2:
    print("Diagonal amplada-profunditat", diagonal3)
elif diagonal1 == diagonal2 and diagonal1 > diagonal3:
    print("Diagonal altura-amplada i diagonal altura-profunditat", diagonal1, diagonal2)
elif diagonal3 == diagonal2 and diagonal2 > diagonal1:
    print("Diagonal amplada-profunditat i diagonal altura-profunditat", diagonal3, diagonal2)
elif diagonal1 == diagonal3 and diagonal1 > diagonal2:
    print("Diagonal altura-amplada i diagonal amplada-profunditat", diagonal1, diagonal3)
elif diagonal1 == diagonal2 and diagonal1 == diagonal3:
    print("Diagonal altura-amplada, diagonal altura-profunditat i diagonal amplada-profunditat", diagonal1, diagonal2, diagonal3)