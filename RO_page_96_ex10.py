#RO_page_96_ex10

costat1 = float(input("costat1 = "))
costat2 = float(input("costat2 = "))
costat3 = float(input("costat3 = "))

if costat1 == costat2 == costat3:
    print("Equilàter")
elif costat1 == costat2 and costat1 != costat3:
    print("Isòceles")
elif costat1 == costat3 and costat1 != costat2:
    print("Isòceles")
elif costat2 == costat3 and costat2 != costat1:
    print("Isòceles")
elif costat1 != costat2 and costat1 != costat3 and costat2 != costat3:
    print("Escalè")