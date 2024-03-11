#RO_page96_ex9

n1 = float(input("n1 = "))
n2 = float(input("n2 = "))
n3 = float(input("n3 = "))

if n1 > n2 and n2 > n3:
    print("Nota màxima = ", n1)
    print("Nota mínima = ", n3)
elif n1 > n2 and n3 > n2:
    print("Nota màxima = ", n1)
    print("Nota mínima = ", n2)
elif n2 > n3 and n3 > n1:
    print("Nota màxima = ", n2)
    print("Nota mínima = ", n1)
elif n2 > n1 and n1 > n3:
    print("Nota màxima = ", n2)
    print("Nota mínima = ", n3)
elif n3 > n2 and n2 > n1:
    print("Nota màxima = ", n3)
    print("Nota mínima = ", n1)
elif n3 > n1 and n1 > n2:
    print("Nota màxima = ", n3)
    print("Nota mínima = ", n2)
    
elif n1 == n2 and n2 > n3:
    print("Nota màxima = ", n1, "i", n2)
    print("Nota mínima = ", n3)
elif n1 == n3 and n3 > n2:
    print("Nota màxima = ", n1, "i", n3)
    print("Nota mínima = ", n2)
elif n3 == n2 and n3 > n1:
    print("Nota màxima = ", n2, "i", n3)
    print("Nota mínima = ", n1)

elif n1 > n2 and n2 == n3:
    print("Nota màxima = ", n1)
    print("Nota mínima = ", n2, "i", n3)
elif n2 > n1 and n1 == n3:
    print("Nota màxima = ", n2)
    print("Nota mínima = ", n1, "i", n3)
elif n3 > n2 and n2 == n1:
    print("Nota màxima = ", n3)
    print("Nota mínima = ", n1, "i", n2)
    
elif n3 == n2 and n2 == n1:
    print("Notes màximes i mínimes", n1, n2, n3)