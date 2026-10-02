import math
import json

print("Calculator v1.6.0\n") 
print("This is a prototype. Please report any bugs.\n")
print("PS: Only two numbers can be used in each calculation.\n")

try: # save history and load only the last 100 calculations to prevent the file from becoming too large.
    with open("history.json", "r") as file:
        history = json.load(file)[-100:]
except (FileNotFoundError, json.JSONDecodeError):
    history = []

mode = input("Input which calculation you would like to use (+, -, *, /, ^, %, sqrt, log, sin, cos, tan, abs, round, angles, !, history, quit, clear): ")

operations = ["+", "-", "*", "/", "^", "%", "sqrt", "log", "sin", "cos", "tan", "abs", "round", "angles", "!", "history", "quit", "clear"]

def get_number(prompt): # function to get a valid number from the user.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def angle_mode(): # function to determine the angle mode and return the appropriate conversion function.
    global ang
    while True:
        if ang == "degrees":
            return math.radians
        elif ang == "radians":
            return lambda x: x
        else:
            print("Invalid input. Please enter 'degrees' or 'radians'.")
            ang = input("Which angle unit would you like to use?\n Degrees \n Radians\n").lower()

ang = "radians" # defines the default angle mode to prevent NameError.

while mode in operations: # main loop to perform calculations based on user input.
    if mode == "+": # addition
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        result = num1 + num2
        print("The result is: ", result)
        history.append(f"{num1} + {num2} = {result}")

    elif mode == "-": # subtraction
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        result = num1 - num2
        print("The result is: ", result)
        history.append(f"{num1} - {num2} = {result}")

    elif mode == "*": # multiplication
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        result = num1 * num2
        print("The result is: ", result)
        history.append(f"{num1} * {num2} = {result}")

    elif mode == "/": # division
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = num1 / num2
        print("The result is: ", result)
        history.append(f"{num1} / {num2} = {result}")

    elif mode == "^": # exponentiation
        base = get_number("Enter the base number: ")
        exponent = get_number("Enter the exponent number: ")
        result = math.pow(base, exponent)
        print("The result is: ", result)
        history.append(f"{base} ^ {exponent} = {result}")

    elif mode == "%": # modulus
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = num1 % num2
        print("The result is: ", result)
        history.append(f"{num1} % {num2} = {result}")

    elif mode == "sqrt": # square root
        num = get_number("Enter the number to find the square root of: ")
        if num < 0:
            print("Error: Cannot compute square root of a negative number.")
            continue
        result = math.sqrt(num)
        print("The square root is: ", result)
        history.append(f"sqrt({num}) = {result}")

    elif mode == "log": # logarithm
        num = get_number("Enter the number to find the logarithm of: ")
        if num <= 0:
            print("Error: Logarithm is not defined for zero or negative numbers.")
            continue
        result = math.log(num)
        print("The logarithm is: ", result)
        history.append(f"log({num}) = {result}")

    elif mode == "sin": # sine
        num = get_number("Enter the number to find the sine of: ")
        result = math.sin(angle_mode()(num))
        print("The sine is: ", result)
        history.append(f"sin({num}) = {result}")

    elif mode == "cos": # cosine
        num = get_number("Enter the number to find the cosine of: ")
        result = math.cos(angle_mode()(num))
        print("The cosine is: ", result)
        history.append(f"cos({num}) = {result}")

    elif mode == "tan": # tangent
        num = get_number("Enter the number to find the tangent of: ")
        result = math.tan(angle_mode()(num))
        print("The tangent is: ", result)
        history.append(f"tan({num}) = {result}")

    elif mode == "round": # rounding
        num = get_number("Enter the number to round: ")
        result = round(num)
        print("The rounded value is: ", result)
        history.append(f"round({num}) = {result}")

    elif mode == "angles": # angle unit selection
        ang = input("Which angle unit would you like to use?\n Degrees \n Radians\n").lower()
        if ang == "degrees": # degrees
            print("Angle unit set to degrees.")

        elif ang == "radians": # radians
            print("Angle unit set to radians.")

        else:
            print("Invalid input. Please enter 'degrees' or 'radians'.")
            continue

    elif mode == "!": # factorial
        num = get_number("Enter the number to find the factorial of: ")
        if num < 0 or not num.is_integer():
            print("Error: Factorial is only defined for non-negative integers.")
            continue
        result = math.factorial(int(num))
        print("The factorial is: ", result)
        history.append(f"{int(num)}! = {result}")

    elif mode == "abs": # absolute number
        num = get_number("Enter the number to find the absolute value of: ")
        result = abs(num)
        print("The absolute value is: ", result)
        history.append(f"abs({num}) = {result}")

    elif mode == "history": # display calculation history
        if not history:
            print("No calculations have been performed yet.")
        else:
            print("Calculation History:")
            for entry in history:
                print(entry)

    elif mode == "quit": # exit the program
        break

    elif mode == "clear": # clear calculation history
        history = []
        print("History cleared.")

    else:
        print("How Did We Get Here?") # Excuse me what the f*cc

    mode = input("Input which calculation you would like to use (+, -, *, /, ^, %, sqrt, log, sin, cos, tan, abs, round, angles, !, history, quit, clear): ")

if mode not in operations:
    print("Invalid input. Please try again.")
    mode = input("Input which calculation you would like to use (+, -, *, /, ^, %, sqrt, log, sin, cos, tan, abs, round, angles, !, history, quit, clear): ")

with open("history.json", "w") as file: # save the calculation history to a .json file.
    json.dump(history, file)
