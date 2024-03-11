#RO_pag216_sumapares

n = int(input("n = "))
v = []
s = 0

for i in range(1,n+1):
    x = int(input("x = "))
    v = v + [x]
for e in v:
    if e%2 == 0:
        s = s + e
    else:
        s = s
print(s)