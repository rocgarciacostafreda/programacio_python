#RO_page_146_ex4

a = int(input("a = "))
b = int(input("b = "))

v = 0
m = 0
if a < b:
    v = a
elif b < a:
    v = b
elif a == b:
    v = a

m = v
while a%v != 0 or b%v != 0:
    v = v - 1
    m = v
print("m = ", m)