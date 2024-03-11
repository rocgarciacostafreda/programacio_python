#rgarcia_3.py
#apartat_a
h = float(input("h(en mm) = "))
ti = float(input("ti(en ºC) = "))
tf = float(input("tf(en ºC) = "))
ce = float(input("ce(en KJ/(kg * ºC) = "))

dt = tf - ti
h = h/100

m = 7.5 * 12.5 * h

ea = m * ce * dt

print("Ea = ", ea, "kJ")
#apartat_b

h = float(input("h(en mm) = "))
m = 7.5 * 12.5 * h
ce = 4.187
dt = 20

ea = m * ce * dt
print("ea ", ea)

h = float(input("h(en mm) = "))
m = 7.5 * 12.5 * h
ce = 4.187
dt = 20

ea = m * ce * dt
print("ea ", ea)

h = float(input("h(en mm) = "))
m = 7.5 * 12.5 * h
ce = 4.187
dt = 20

ea = m * ce * dt
print("ea ", ea)

h = float(input("h(en mm) = "))
m = 7.5 * 12.5 * h
ce = 4.187
dt = 20

ea = m * ce * dt
print("ea ", ea)

#si es posa cada valor d'ea per valor d'h en una gràfica surt una recta que passa per (0,0).

#apartat_c

cmin = 31.4025 * (1/45.79) * (12.94/12.5)
print("Cost mínim = ", cmin, "€")