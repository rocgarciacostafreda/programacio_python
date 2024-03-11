#RO_page_45_ejemplo4

a = int(input(" a = ",))
b = int(input(" b = ",))
x = 0

if a < 5 :
    x = x + a - b
    print (" x = ", x)
else :
    x = x + a
    while x < b:
        x = x + a

    print (" x = ", x)