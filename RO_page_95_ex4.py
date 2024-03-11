#RO_page_95_ex4

from math import*

n = int(input("n = "))

x = n//10
y = n%10
z = x + y
if z * pow(-1,z) > 0:
    print(z , "parell")
else:
    print(z , "imparell")