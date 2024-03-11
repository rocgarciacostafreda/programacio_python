#RO_page_96_ex13

horesju = float(input("Hores Juan = "))
salariju = float(input("Salari Juan = "))
descomptesju = float(input("Descomptes Juan(en percentatge) = "))

horespe = float(input("Hores Pedro = "))
salaripe = float(input("Salari Pedro = "))
descomptespe = float(input("Descomptes Pedro(en percentatge) = "))

horesjo = float(input("Hores José = "))
salarijo = float(input("Salari José = "))
descomptesjo = float(input("Descomptes José(en percentatge) = "))

descomptesju = descomptesju/100
descomptespe = descomptespe/100
descomptesjo = descomptesjo/100

guanysju = horesju * salariju * descomtesju
guanyspe = horespe * salaripe * descomptespe
guanysjo = horesjo * salarijo * descomptesjo

if guanysju > guanyspe and guanysju > guanyspe:
    print("Juan ", guanysju, "$")
elif guanyspe > guanysju and guanyspe > guanysjo:
    print("Pedro ", guanyspe, "$")
elif guanysjo > guanysju and guanysjo > guanyspe:
    print("José ", guanysjo, "$")
elif guanysju == guanyspe and guanyspe > guanysjo:
    print("Juan i Pedro ", guanyspe, "$")
elif guanyspe == guanysjo and guanyspe > guanysju:
    print("Pedro i José ", guanyspe, "$")
elif guanysjo == guanysju and guanyspe < guanysjo:
    print("Juan i José ", guanysju, "$")
elif guanyspe == guanysju and guanyspe == guanysjo:
    print("Pedro, Juan i José ", guanyspe, "$")