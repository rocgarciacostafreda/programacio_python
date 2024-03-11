#RO_page_181_ex13_coordenades_convertir

from math import*

def polar(x,y):
    r = sqrt((x**2)+(y**2))
    t = ((atan(y/x)*180)/(2*pi))
    
    return r,t

def cartesiana(r,t):
    x = r*cos(t)
    y = r*sin(t)
    
    return x,y


print("Escull que vols convertir i a què")
print("")
print("1. Convertir de cartesià a polar")
print("2. Convertir de polar a cartesià")
tria = int(input("Tria la opció "))

if tria == 1:
    x = float(input("x = "))
    y = float(input("y = "))
    r,t = polar(x,y)
    print("Les coordenades polars són",r,t)
elif tria == 2:
    r = float(input("r = "))
    t = float(input("t = "))
    x,y = cartesiana(r,t)
    print("Les coordenades cartesianes són",x,y)
elif tria == 3:
    print("Numero triat no vàlid")