import math
import json

print("Calculator v1.5.4\n")
print("This is a prototype. Please report any bugs.\n")
print("PS: PEMDAS is not supported. Parentheses, too, are not.\n")

try:
    with open("history.json", "r") as file:
        history = json.load(file)
except FileNotFoundError:
    history = []

mode = input("Input which calculation you would like to use (+, -, *, /, ^, sqrt, log, sin, cos, tan, history, quit): ")

operations = ["+", "-", "*", "/", "^", "sqrt", "log", "sin", "cos", "tan", "history", "quit"]

while mode in operations:
    if mode == "+":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print("The result is: ", result)
        history.append(f"{num1} + {num2} = {result}")

    elif mode == "-":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print("The result is: ", result)
        history.append(f"{num1} - {num2} = {result}")

    elif mode == "*":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        print("The result is: ", result)
        history.append(f"{num1} * {num2} = {result}")

    elif mode == "/":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = num1 / num2
        print("The result is: ", result)
        history.append(f"{num1} / {num2} = {result}")

    elif mode == "^":
        base = float(input("Enter the base number: "))
        exponent = float(input("Enter the exponent number: "))
        result = math.pow(base, exponent)
        print("The result is: ", result)
        history.append(f"{base} ^ {exponent} = {result}")

    elif mode == "sqrt":
        num = float(input("Enter the number to find the square root of: "))
        if num < 0:
            print("Error: Cannot compute square root of a negative number.")
            continue
        result = math.sqrt(num)
        print("The square root is: ", result)
        history.append(f"sqrt({num}) = {result}")

    elif mode == "log":
        num = float(input("Enter the number to find the logarithm of: "))
        if num <= 0:
            print("Error: Logarithm is not defined for zero or negative numbers.")
            continue
        result = math.log(num)
        print("The logarithm is: ", result)
        history.append(f"log({num}) = {result}")

    elif mode == "sin":
        num = float(input("Enter the number to find the sine of: "))
        result = math.sin(num)
        print("The sine is: ", result)
        history.append(f"sin({num}) = {result}")

    elif mode == "cos":
        num = float(input("Enter the number to find the cosine of: "))
        result = math.cos(num)
        print("The cosine is: ", result)
        history.append(f"cos({num}) = {result}")

    elif mode == "tan":
        num = float(input("Enter the number to find the tangent of: "))
        result = math.tan(num)
        print("The tangent is: ", result)
        history.append(f"tan({num}) = {result}")

    elif mode == "history":
        if not history:
            print("No calculations have been performed yet.")
        else:
            print("Calculation History:")
            for entry in history:
                print(entry)

    elif mode == "quit":
        break

    else:
        print("Invalid input. Please try again.")

    mode = input("Input which calculation you would like to use (+, -, *, /, ^, sqrt, log, sin, cos, tan, history, quit): ")

if mode not in operations:
    print("Invalid input. Please try again.")
    mode = input("Input which calculation you would like to use (+, -, *, /, ^, sqrt, log, sin, cos, tan, history, quit): ")

with open("history.json", "w") as file:
    json.dump(history, file)
