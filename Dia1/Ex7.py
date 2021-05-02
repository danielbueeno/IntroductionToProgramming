num1 = float(input("Number 1: "))
operator = input("Operator: ")
num2 = float(input("Number 2: "))


if(operator == '+'):
    print("Result:",(num1+num2))
elif(operator == "-"):
    print("Result:",(num1-num2))
elif(operator == '*'):
    print("Result:",(num1*num2))
elif(operator == "/"):
    print("Result:",(num1/num2))
else:
    print("Invalid operator!")
