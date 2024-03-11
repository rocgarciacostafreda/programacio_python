#rgarcia_challenge_ex3

def cons(ncons,dcons,acons):
    if dcons < 10 or dcons > 30:
        print("Error de dades")
    elif acons < 10 or acons > 50:
        print("Error de dades")
    elif ncons == 1:
        distancia = 0
    elif ncons > 1:
        distancia = ((ncons-2)*acons) + (dcons*(cons-1))
        print("La distància entre cons equival a ",distancia, "cm")
    
    
print("Totes les distàncies insertades al programa hauran de ser en centímetres(cm)")
print("Les distàncies entre cons han de ser entre 10 i 30 cm")
print("L'amplada dels cons ha de ser de 10 a 50 cm")
ncons = int(input("numero de cons = "))
dcons = int(input("distància entre cons = "))
acons = int(input("amplada cons = "))

x = cons(ncons,dcons,acons)
