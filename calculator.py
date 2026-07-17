#There is a current limit to how many numbers can be added
while True:
    number1=float(input("enter first number here:"))
    number2=float(input("enter second number here:"))
    operation=input("choose an operation (+,-,*,/,**,//,%):") #choose the operation you want
    if operation == "+":
        print(number1+number2)
    elif operation == "-":
        print(number1-number2)
    elif operation == "*":
        print(number1*number2)
    elif operation == "/":
        print(number1/number2)
    elif operation == "**":
        print(number1**number2)
    elif operation == "//":
        print(number1//number2)
    elif operation == "%":
        print(number1%number2)
    else:
        print("invalid")
    again=input("Do you wanna do another calculation? (y/n):")
    if again == "n":
        break
