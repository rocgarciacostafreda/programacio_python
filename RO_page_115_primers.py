#RO_page_115_primers
while True:
    n = int(input("n = "))
    x = 2
    m = n%x
    while x < n:
    
        if m == 0:
            print("El nombre", n, "no és primer")
            break
        else:
            x = x + 1
            x == n
    print("És nombre primer")