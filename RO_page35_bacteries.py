#RO_page35_bacterias

x = int(input("Nombre de bacteries = ",))
m = int(input("Nombre màxim de bacteries = ",))
d = 0

while x <= m :
    x = 2 * x
    d = d + 1
    
print ("Dies = ", d)