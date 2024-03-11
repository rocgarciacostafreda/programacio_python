#RO_page_83_ex1

from math import*

dies = int(input("Dies = "))

anys = dies//365
dies_restants = dies%365
mesos = dies_restants//30
dies_finals = dies_restants%30

print(anys, "anys", mesos, "mesos", dies_finals, "dies")