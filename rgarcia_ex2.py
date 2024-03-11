#rgarcia_challenge_ex2

dia = int(input("dia = "))
mes = int(input("mes = "))
Any = int(input("any = "))

suma1 = dia + mes + Any


n1 = suma1//1000
n2 = (suma1//10)%10
n3 = ((suma1//10)//10)%10
n4 = suma1%10

suma2 = n1 + n2 + n3 + n4

m1 = suma2//10
m2 = suma2%10

tarot = m1 + m2
if dia > 31 and mes == 1:
    print("Aquesta data és incorrecta")
elif dia > 29 and mes == 2:
    print("Aquesta data és incorrecta")
elif dia > 31 and mes == 3:
    print("Aquesta data és incorrecta")
elif dia > 30 and mes == 4:
    print("Aquesta data és incorrecta")
elif dia > 31 and mes == 5:
    print("Aquesta data és incorrecta")
elif dia > 30 and mes == 6:
    print("Aquesta data és incorrecta")
elif dia > 31 and mes == 7:
    print("Aquesta data és incorrecta")
elif dia > 31 and mes == 8:
    print("Aquesta data és incorrecta")
elif dia > 30 and mes == 9:
    print("Aquesta data és incorrecta")
elif dia > 31 and mes == 10:
    print("Aquesta data és incorrecta")
elif dia > 30 and mes == 11:
    print("Aquesta data és incorrecta")
elif dia > 31 and mes == 12:
    print("Aquesta data és incorrecta")
elif mes > 12:
    print("Aquesta data és incorrecta")
else:
    print("El teu nombre tarot és el ",tarot)
    