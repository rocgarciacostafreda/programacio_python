#RO_page_97_ex_22

x = float(input("x = "))
a = float(input("a = "))
b = float(input("b = "))

if x > a and x > b:
    print("Més gran que a i b")
elif x > a and x < b:
    print("Entre a i b")
elif x < a and x < b:
    print("Més petit que a i b")