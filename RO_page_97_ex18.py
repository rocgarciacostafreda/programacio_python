#RO_page_97_ex18

p = float(input("P = "))
t = float(input("T = "))

imc = p/(t**2)

if imc < 20:
    print("Desnutrido")
elif imc >= 20 and imc < 25:
    print("Normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 35:
    print("Obesidad grado 1")
elif imc >= 35 and imc < 40:
    print("Obesidad grado 2")
elif imc >= 40:
    print("Obesidad grado 3")