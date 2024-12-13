
num1 = int(input("please input the first number"))
num2 = int(input("please input the second number"))
operation = input("please input the operation")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("invalid operation")