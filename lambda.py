names=["Daniela Pérez","Casandra Claro","Danilo Hernández","Sandra Vásquez"]
lnames= [(lambda name: name.split(" ")[1])(name) for name in names]
print(lnames)

names.sort(key=lambda fname: fname.split(" ")[-1].lower())
print(names)

def cuadratic_finction(a,b,c):
	return lambda x:a*x**2+b*x+c
print(cuadratic_finction(2,3,5)(1))