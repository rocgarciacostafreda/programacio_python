#RO_page_96_ex8

nota1_1 = float(input("nota1_1 = "))
nota1_2 = float(input("nota1_2 = "))
nota1_3 = float(input("nota1_3 = "))

nota2_1 = float(input("nota2_1 = "))
nota2_2 = float(input("nota2_2 = "))
nota2_3 = float(input("nota2_3 = "))

if nota1_1 > nota1_2 and nota1_3 > nota1_2:
    nota = nota1_1 + nota1_3
    print(nota)
elif nota1_1 > nota1_3 and nota1_2 > nota1_3:
    nota = nota1_1 + nota1_2
    print(nota)
elif nota1_2 > nota1_1 and nota1_3 > nota1_1:
    nota = nota1_3 + nota1_2
    print(nota)
elif nota1_1 == nota1_2 and nota1_1 > nota1_3:
    nota = nota1_1 + nota1_2
    print(nota)
elif nota1_1 > nota1_2 and nota1_1 == nota1_3:
    nota = nota1_1 + nota1_3
    print(nota)
elif nota1_2 > nota1_1 and nota1_2 == nota1_3:
    nota = nota1_2 + nota1_3
    print(nota)
    
    
if nota2_1 > nota2_2 and nota2_3 > nota2_2:
    nota2 = nota2_1 + nota2_3
    print(nota2)
elif nota2_1 > nota2_3 and nota2_2 > nota2_3:
    nota2 = nota2_1 + nota2_2
    print(nota2)
elif nota2_2 > nota2_1 and nota2_3 > nota2_1:
    nota2 = nota2_3 + nota2_2
    print(nota2)
elif nota2_1 == nota2_2 and nota2_1 > nota2_3:
    nota2 = nota1_1 + nota1_2
    print(nota2)
elif nota2_1 > nota2_2 and nota2_1 == nota2_3:
    nota2 = nota1_1 + nota1_3
    print(nota2)
elif nota2_2 > nota2_1 and nota2_2 == nota2_3:
    nota2 = nota2_2 + nota2_3
    print(nota2)