#RO_page_97_ex17

p = float(input("P = "))
t = float(input("T = "))

imc = p/(t**2)

if imc < 18.5:
    print(imc, "Desnutrido")
elif imc >= 18.5 and imc < 25.5:
    print(imc, "Peso normal")
elif imc >= 25.5:
    print(imc, "Sobrepeso")