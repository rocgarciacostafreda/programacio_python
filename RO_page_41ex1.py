#RO_page_41ex1

num_paquets = 10
pes_maxim = 0

for comptador in range (1, num_paquets +1, 1):
    print("Pes del paquet", comptador, "en kg")
    pes_paquets = float(input())
    if pes_paquets > pes_maxim:
        pes_maxim = pes_paquets
print("Pes màxim =", pes_maxim)