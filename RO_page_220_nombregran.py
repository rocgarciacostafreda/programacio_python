#RO_page_220_nombregran
v = [1,2,3,2,6,1]
def vectmax(v):
    n=len(v)
    r=v[0]
    p=0
    for i in range(1,n):
        if v[i]>r:
            r=v[i]
            p=i
    return [r,p]
[r,p]=vectmax(v)
print(r)
print(p)