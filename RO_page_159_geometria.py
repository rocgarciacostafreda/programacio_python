#RO_page_159_geometria
from math import*
def quadrat(a):
    A = a**2
    P = a * 4
    print("Area = ",A)
    print("Perímetre = ", P)
def triangle(a,b,c,h):
    A = (b * h)/2
    P = a + b + c
    print("Area = ",A)
    print("Perímetre = ", P)
def rectangle(a,b):
    A = b * a
    P = (2 * a) + (2 * b)
    print("Area = ",A)
    print("Perímetre = ", P)
def paralelogram(b,h,a):
    A = b * h
    P = 2 * (b + a)
    print("Area = ",A)
    print("Perímetre = ", P)
def rombo(D, d, a):
    A = (D * d)/2
    P = 4 * a
    print("Area = ",A)
    print("Perímetre = ", P)
def estel(D,d,a,b):
    A = (D * d) / 2
    P = 2 * (a + b)
    print("Area = ",A)
    print("Perímetre = ", P)
def trapezi (a,b,B,c,h):
    A = ((b + B) * h)/2
    P = B + b + a + c
    print("Area = ",A)
    print("Perímetre = ", P)
def cercle (r):
    A = pi * (r)**2
    P = 2 * pi * r
    print("Area = ",A)
    print("Perímetre = ", P)
def poligon_regular (a,b,n):
    P = n * b
    A = (P * a)/2
    print("Area = ",A)
    print("Perímetre = ", P)
def corona_circular (R,r):
    A = pi * ((R**2) - (r**2))
    print("Area = ",A)
def cub (a):
    A = 6 * (a**2)
    V= a ** 3
    print("Area = ",A)
    print("Volum = ", V)
def cilindre(R, h):
    A = 2*pi*r*(h + R)
    V = pi * h * (R**2)
    print("Area = ",A)
    print("Volum = ", V)
def ortoedre(a,b,c):
    A = 2 * ((a * b) + (a*c) + (b * c))
    V = a * b * c
    print("Area = ",A)
    print("Volum = ", V)
def sector_circular (R,n):
    A = (pi * (R ** 2) * n)/360
    print("Area = ",A)
def prisme_recte(P,h,a,Ab):
    A = P * (h + a)
    V = Ab * h
    print("Area = ",A)
    print("Volum = ", V)
def con(R,g,h):
    A = pi * R *(R + g)
    V = (pi * R**2 * h)/3
    print("Area = ",A)
    print("Volum = ", V)
def tronc_con(R,r,h,g):
    A = pi*(g*(r + R) + (r**2) + (R**2))
    V = (pi * h *((R**2)+(r**2)+(R*r)))/3
    print("Area = ",A)
    print("Volum = ", V)
def esfera(R):
    A = 4 * pi * (R**2)
    V = (4 * pi * (R**3))/3
    print("Area = ",A)
    print("Volum = ", V)
def piramide(P,a,a2,h,Ab):
    A = (P * (a + a2))/2
    V = (Ab * h)/3
    print("Area = ",A)
    print("Volum = ", V)
def tetraedre_regular(a):
    A = (a**2)* sqrt(3)
    V = ((a**3) * sqrt(2))/12
    print("Area = ",A)
    print("Volum = ", V)
def octaedre_regular(a):
    A = (a**2)*2*sqrt(3)
    V = ((a**3) * sqrt(2))/3
    print("Area = ",A)
    print("Volum = ", V)
def tronc_piramide(p,P,a,ab,AB,h):
    A=((p+P)/2)*a+ab+AB
    V=(ab+AB+sqrt(ab*AB))*h/3
    print("Area = ",A)
    print("Volum = ", V)
def casquet_esferic(r,h):
    A=2*pi*r*h
    V=(pi*(h**2)*(3*r-h))/3
    print("Area = ",A)
    print("Volum = ", V)
def cunya_esferica(n,r):
    A=4*pi*pow(r,2)*n/360
    V=(4*pi*pow(r,3)*n)/3*360
    print("Area = ",A)
    print("Volum = ", V)
def segment_esferic(h,r,r1,R):
    A=2*pi*R*h
    V = (pi*h*(pow(h,2)+3*pow(r,2)+3*pow(r1,2)))/6
    print("Area = ",A)
    print("Volum = ", V)
x = False
while x == False:
    print("")
    print("Escull entre aquestes figures:")
    print("1. Quadrat")
    print("2. Triangle")
    print("3. Rectangle")
    print("4. Paralelogram")
    print("5. Rombe")
    print("6. Estel")
    print("7. Trapezi")
    print("8. Cercle")
    print("9. Polígon Regular")
    print("10. Corona circular")
    print("11. Sector circular")
    print("12. Cub")
    print("13. Cilindre")
    print("14. Ortoedre")
    print("15. Prisme recte")
    print("16. Con")
    print("17. Tronc de con")
    print("18. Esfera")
    print("19. Piràmide")
    print("20. Tetraedre regular")
    print("21. Octoedre regular")
    print("22. Tronc de piràmide")
    print("23. Casquet esfèric")
    print("24. Cunya esfèrica")
    print("25. Segment esfèric")
    print("")
    d = int(input("d = "))
    if d == 1:
        a = float(input("a = "))
        quadrat(a)
    elif d == 2:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        h = float(input("h = "))
        triangle(a,b,c,h)
    elif d == 3:
        a = float(input("a = "))
        b = float(input("b = "))
        rectangle(a,b)
    elif d == 4:
        b = float(input("b = "))
        h = float(input("h = "))
        a = float(input("a = "))
        paralelogram(b,h,a)
    elif d == 5:
        D = float(input("D = "))
        d = float(input("d = "))
        a = float(input("a = "))
        rombo(D,d,a)
    elif d == 6:
        D = float(input("D = "))
        d = float(input("d = "))
        a = float(input("a = "))
        b = float(input("b = "))
        estel(D,d,a,b)
    elif d == 7:
        a = float(input("a = "))
        b = float(input("b = "))
        B = float(input("B = "))
        c = float(input("c = "))
        h = float(input("h = "))
        trapezi(a,b,B,c,h)
    elif d == 8:
        r = float(input("r = "))
        cercle(r)
    elif d == 9:
        a = float(input("a = "))
        b = float(input("b = "))
        n = float(input("n = "))
        poligon_regular(a,b,n)
    elif d == 10:
        r = float(input("r = "))
        R = float(input("R = "))
        corona_circular(R,r)
    elif d == 11:
        a = float(input("a = "))
        cub(a)
    elif d == 12:
        R = float(input("R = "))
        h = float(input("h = "))
        cilindre(R,h)
    elif d == 13:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        ortoedre(a,b,c)
    elif d == 14:
        R = float(input("R = "))
        n = float(input("n = "))
        sector_circular(R,n)
    elif d == 15:
        P = float(input("P = "))
        h = float(input("h = "))
        a = float(input("a = "))
        Ab = float(input("Ab = "))
        prisme_recte(P,h,a,Ab)
    elif d == 16:
        R = float(input("R = "))
        g = float(input("g = "))
        h = float(input("h = "))
        con(R,g,h)
    elif d == 17:
        R = float(input("R = "))
        r = float(input("r = "))
        h = float(input("h = "))
        g = float(input("g = "))
        tronc_con(R,r,h,g)
    elif d == 18:
        R = float(input("R = "))
        esfera(R)
    elif d == 19:
        P = float(input("P = "))
        a = float(input("a = "))
        a2 = float(input("a2 = "))
        h = float(input("h = "))
        Ab = float(input("Ab = "))
        piramide(P,a,a2,h,Ab)
    elif d == 20:
        a = float(input("a = "))
        tetraedre_regular(a)
    elif d == 21:
        a = float(input("a = "))
        octaedre_regular(a)
    elif d == 22:
        p = float(input("p = "))
        P = float(input("P = "))
        a = float(input("a = "))
        ab = float(input("ab = "))
        AB = float(input("AB = "))
        h = float(input("h = "))
        tronc_piramide(p,P,a,ab,AB,h)
    elif d == 23:
        r = float(input("r = "))
        h = float(input("h = "))
        casquet_esferic(r,h)
    elif d == 24:
        n = float(input("n = "))
        r = float(input("r = "))
        cunya_esferica(n,r)
    elif d == 25:
        h = float(input("h = "))
        r = float(input("r = "))
        r1 = float(input("r1 = "))
        R = float(input("R = "))
        segment_esferic(h,r,r1,R)
