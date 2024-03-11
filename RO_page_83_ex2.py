#RO_page_83_ex2

from math import*

dies_inicials = int(input("Dies = "))

mesos = dies_inicials//30
dies_sobrants = dies_inicials%30
setmanes = dies_sobrants//7
dies = dies_sobrants%7

print(mesos, "mesos", setmanes, "setmanes", dies, "dies")