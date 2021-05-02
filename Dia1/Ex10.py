print("This program calculates odd numbers in a range.")
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

for i in range(number1, number2):
    if( i % 2 != 0):
        print(i)
