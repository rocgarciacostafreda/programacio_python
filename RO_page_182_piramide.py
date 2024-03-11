#RO_page_182_piramide

def piramide(n):
    i = 1
    f = 0
    for e in range(1,n+1):
        f = f + i
        i = i + 1
    return(e,f)
n = int(input("n = "))
(e,x) = piramide(n)
print("En la priàmide número", e, "hi ha ", x, " boles")