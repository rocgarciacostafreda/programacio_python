#RO_page_146_ex1

n = int(input("n = "))

x = 0
y = 0
pes_maxim = 0
pes_minim = 10**99

while x < n :
    p = float(input("p = "))
    print("p", x, "=", p, "kg")
    x = x + 1
    y = y + p
    if p >= pes_maxim:
        pes_maxim = p
    elif p < pes_minim:
        pes_minim = p
promig = y/n
print("promig = ", promig)
print("pes mínim = ", pes_minim)
print("pes màxim = ", pes_maxim)    