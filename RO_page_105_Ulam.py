#RO_page_105_Ulam

x = int(input("x = "))
while x > 1:
    if x%2 == 0:
        x = x/2
    else:
        x = 3 * x + 1
    print(x)