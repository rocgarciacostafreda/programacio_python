#RO_page_97_ex15

from math import*

n = int(input("n = "))

n1 = n//100
n = n%100
n2 = n//10
n3 = n%10
m = n1 * n2
m1 = m//10
m2 = m%10
if m2 == n3:
    print("Si que compleix la fórmula")
elif m2 != n3:
    print("No compleix la fórmula")