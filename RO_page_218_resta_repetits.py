#RO_page_218_restarepetits

n = int(input("n = "))
v = []
u = []
for i in range(1,n+1):
    x = int(input("x = "))
    v = v + [x]
print(v)

for e in v:
    if e not in u:
        u = u + [e]
    else:
        u = u
print(u)