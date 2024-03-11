#RO_page25_notes

nota_examen = float(input("nota_examen="))
nota_lliçons = float(input("nota_lliçons = "))
nota_feina1 = float(input("nota_feina1 = "))
nota_feina2 = float(input("nota_feina2 = "))
nota_feina3 = float(input("nota_feina3 = "))

nota_final = (nota_examen * 0.7) + (nota_lliçons * 2) + (((nota_feina1*10) + (nota_feina2*10)+ (nota_feina3*10))/30)

print ("nota_final = ", nota_final)