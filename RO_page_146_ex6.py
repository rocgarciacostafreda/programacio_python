#RO_page_146_ex6

n = int(input("n = "))

x = 0
candidat1 = 0
candidat2 = 0
candidat3 = 0
blanc = 0
nul = 0
while x < n:
    vot = int(input("vot = "))
    if vot == 0:
        blanc = blanc + 1
    elif vot == 1:
        candidat1 = candidat1 + 1
    elif vot == 2:
        candidat2 = candidat2 + 1
    elif vot == 3:
        candidat3 = candidat3 + 1
    else:
        nul = nul + 1
    x = x + 1
print("Vots nuls = ", nul, "Vots en blanc = ", blanc, "Candidat 1 = ", candidat1, "Candidat 2 = ", candidat2, "Candidat 3 = ", candidat3)