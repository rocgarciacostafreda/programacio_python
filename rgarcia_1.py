#rgarcia_1.py

i= 0
sou = float(input("sou = "))

if sou < 10000:
    sou = 0.95 * sou
    print("Sou restant = ", sou, "€")
elif sou >= 10000 and sou < 20000:
    sou = 0.85 * sou
    print("Sou restant = ", sou, "€")
elif sou >= 20000 and sou < 35000:
    sou = 0.8 * sou
    print("Sou restant = ", sou, "€")
elif sou >= 35000 and sou <= 60000:
    sou = 0.7 * sou
    print("Sou restant = ", sou, "€")
elif sou > 60000:
    sou = 0.55 * sou
    print("Sou restant = ", sou, "€")
    
while i < sou:
    sou = float(input("sou = "))
    if sou < 10000:
        sou = 0.95 * sou
        print("Sou restant = ", sou, "€")
    elif sou >= 10000 and sou < 20000:
        sou = 0.85 * sou
        print("Sou restant = ", sou, "€")
    elif sou >= 20000 and sou < 35000:
        sou = 0.8 * sou
        print("Sou restant = ", sou, "€")
    elif sou >= 35000 and sou <= 60000:
        sou = 0.7 * sou
        print("Sou restant = ", sou, "€")
    elif sou > 60000:
        sou = 0.55 * sou
        print("Sou restant = ", sou, "€")