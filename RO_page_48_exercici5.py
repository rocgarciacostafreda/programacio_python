#RO_page_48_exercici5

a = int(input("a = ",))
b = int(input("b = ",))

if not a < 0 :
    while a < b :
        a = a + 1
        b = b - 1
else :
    if b < 0:
        b = 2 * b
    else :
        b = b
print ("a = ", a)
print ("b = ", b)