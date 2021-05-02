print("Insert 3 numbers: ")
num1 = int(input("--> "))
num2 = int(input("--> "))
num3 = int(input("--> "))

if num1 <= num2:
    if num1 <= num3:
        menor = num1
    else:
        menor = num3
else:
    if num2 < num3:
        menor = num2
    else:
        menor = num3

print("Menor:", menor)