#RO_page_46_ejemplo5

a = int(input("a = ",))
b = int(input("b = ",))
c = int(input("c = ",))

if a > b and c > a:
    print ("c = ", c)
elif a > b and a > c:
    while a > c :
        c = c + 3
    print ("c = ",c)
elif a < b:
    a = a + 5
    if a > b + c :
        print ("a = ",a)
        print ("c = ",c)
    else :
        while a < b + c :
            a = a + 5
        print ("a = ", a)
        print ("c = ", c)
        
    