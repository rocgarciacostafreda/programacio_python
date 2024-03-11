#RO_page_96_ex14
from math import*
h = float(input("h = "))
l = float(input("l = "))
d = float(input("d = "))
diametre = float(input("diametre = "))

h_l = sqrt((h**2)+(l**2))
l_d = sqrt((l**2)+(d**2))
h_d = sqrt((h**2)+(d**2))

if h_l < diametre and l_d > diametre and h_d > diametre:
    print("Pot passar")
elif h_l > diametre and l_d > diametre and h_d < diametre:
    print("Pot passar")
elif h_l > diametre and l_d < diametre and h_d > diametre:
    print("Pot passar")
elif h_l < diametre and l_d < diametre and h_d > diametre:
    print("Pot passar")
elif h_l > diametre and l_d < diametre and h_d < diametre:
    print("Pot passar")
elif h_l < diametre and l_d > diametre and h_d < diametre:
    print("Pot passar")
elif h_l < diametre and l_d < diametre and h_d < diametre:
    print("Pot passar")
else:
    print("No pot passar")