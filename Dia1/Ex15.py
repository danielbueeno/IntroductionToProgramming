base = float(input("Base: "))
h = float(input("Altura: "))

if(base<=0 or h<= 0):
    print("Valores inválidos!")
else:
    area = (base*h)/2
    print("Área:", area)
