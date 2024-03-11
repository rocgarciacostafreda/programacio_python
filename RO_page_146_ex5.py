#RO_page_146_ex5

n = int(input("n = "))

x = 1
p = 1
i = 3
y = 1
p2 = 1

while x < n:
    p = p + ((1/i)* (-1)**(y))
    i = i + 2
    x = x + 1
    y = y + 1
p2 = p * 4

print("pi = ", p2)