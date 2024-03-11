#RO_page_146_ex10

n = int(input("n = "))

i = 0
x = 1
suma = 0

while i < n:
    suma = suma + (x**3)
    x = x + 1
    i = i + 1
print("Suma = ", suma)