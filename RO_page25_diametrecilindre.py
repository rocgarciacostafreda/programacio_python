# RO_pag25_diametre_cilindre.py

hight = float(input("hight = "))
volume = float(input("volume (L) = "))
pi = 3.1416

volume = volume / 1000
diameter = ((volume * 4)/(pi*hight)) **0.5

print ("diameter = ", diameter)
