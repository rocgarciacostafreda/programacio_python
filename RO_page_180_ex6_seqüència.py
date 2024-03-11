#RO_page_180_ex6_seqüència

def secuencia1(n):
    suma = 0
    esquerra = 0
    mig = 1
    dreta = 1
    dreta_antic=0
    for n in range(1,n+1):
            print("El nombre ",n," arriba fins a ",dreta)
            suma = suma + dreta
            dreta=esquerra+mig
            dreta_antic=dreta
            esquerra = mig
            mig = dreta_antic

n = int(input("n = "))
secuencia1(n)