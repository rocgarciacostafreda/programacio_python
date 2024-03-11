#RO_page_146_ex11

n = int(input("n = "))

a = 0
primer = 1
segon = 1
tercer = 0

while a < n:
    tercer = primer + segon
    primer = segon
    segon = tercer
    a = a + 1
if n == 1:
    suma = 1
elif n == 2:
    suma = 2
elif n => 3: