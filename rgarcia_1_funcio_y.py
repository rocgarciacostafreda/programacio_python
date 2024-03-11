#rgarcia_1
from math import*
def funcio1(alfa):
    alfa = (alfa*pi)/180
    y = 4 + sin(alfa)
    return y
        
        
def funcio2(alfa):
    alfa = (alfa*pi)/180
    y = 4 + (230*sin(alfa))
    return y

variacio = (pi/2)#aquesta variable és la variació en radiants d'un angle quan l'augmentes 45º
alfa = 0
while True:
    y = funcio1(alfa)
    print("y" "                          " "alfa")
    print(y,"     " ,alfa, " en radians")
    alfa = alfa + variacio
    if alfa > 2*pi:
        break
    
while True:
    y2 = funcio2(alfa)
    print("y2" "                          " "alfa")
    print(y2,"     " ,alfa, " en radians")
    alfa = alfa + variacio
    if alfa > 2*pi:
        break
    
