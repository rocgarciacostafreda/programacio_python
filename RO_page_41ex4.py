#RO_page_41ex4

terminos = int(input("Términos = "))
x = 3
pi_quarts = 1
pi = 1
for n in range (1, terminos):
    if n%2 == 0:
        pi_quarts = pi_quarts + (1/x)*1
    else:
        pi_quarts = pi_quarts + (1/x)*-1
    x = x + 2
pi = pi_quarts * 4
print("Pi = ", pi)