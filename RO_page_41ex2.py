#RO_page41ex2

n = int(input("n = "))
si = 0
no = 0
for comptador in range (1, n + 1, 1):
    print("Vot", comptador, "=")
    vot = int(input())
    if vot == 1:
        si = si + 1
    elif vot == 0:
        no = no + 1
    else:
        si = si
        no = no
print("Vots pel si =", si)
print("Vots pel no =", no)