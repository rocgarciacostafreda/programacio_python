#RO_page_146_ex9

from math import*

n = int(input("n = "))

a = 0
total = 0

while a < n:
    x = float(input("x = "))
    y = float(input("y = "))
    d = sqrt(pow(x,2) + pow(y,2))
    total = total + d
    a = a + 1
print("Total = ", total)