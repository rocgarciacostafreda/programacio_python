# RO_page25_areaivolum_blocrectangular

hight = float(input("hight = "))
width = float(input("width = "))
depth = float(input("depth = "))

area = (((width * hight)*2) + ((width * depth)*2) + ((hight * depth)*2))
volume = (width * hight) * (depth)

print ("area = ", area, "m2")
print ("volume = ", volume, "m3")