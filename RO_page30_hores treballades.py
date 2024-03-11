#RO_page30_horastreballades

c = int(input("c = ",))
t = float(input("t = ",))
d = float(input("d = ",))

p = (c * t) - d
if c >= 40:
    p = (40 * t) + ((c - 40) * 1.5) - d

print ("p = ", p, "€")
