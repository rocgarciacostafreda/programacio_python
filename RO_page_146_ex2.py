#RO_page_146_ex2

n = float(input("n = "))

x = 0
u = x + 1

while x < n :
    p = float(input("p = "))
    print("p", u, "=", p, "kg")
    if p < 10:
        print("Menor a 10 kg")
    elif p >= 10 and p <= 20:
        print("Entre 10 i 20 kg")
    elif p > 20:
        print("Més gran que 20 kg")
    x = x + 1