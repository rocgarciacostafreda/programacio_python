#RO_page_147_ex15

capacitat = 2050
pes = [250, 750, 1000, 1222]
pes_total = 0
n = 0
x = 0
pes.sort()

while x <= capacitat:
    print(pes_total)
    pes_total = pes_total + pes[n]
    n = n + 1
    x = pes_total

    