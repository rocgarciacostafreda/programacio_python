#RO_pag_150_ex37_nombre_auri

n = int(input("n = "))

for a in range (1, n+1):
    for b in range (1, n + 1):
        y = (a+b)/a
        x = a/b
        if y == x:
            print("La parella ",a,b, " és àuria")
        else:
            print(a,b, " no és una parella àuria")