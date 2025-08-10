from math import sqrt

print("calculator version 1.6\n")  
print("REPORT PROBLEMS!\n")

history = []

while True:
    print("Which mode of calculation? (*, /, +, -, exp, sqrt):")  
    mode = input().strip().lower()

    # --- SPECIAL PHASE FOR SQRT ---
    if mode == "sqrt":
        print("\nType the number for a square root:")
        num1 = float(input())
        if num1 >= 0:
            result = sqrt(num1)
        else:
            result = "Error: negative number!"
        print("\nResult:", result)
        history.append(f"√{num1} = {result}")
    else:
        # --- NORMAL OPERATIONS ---
        print("\nType the first number:")  
        num1 = float(input())  
        print("\nType the second number:")  
        num2 = float(input())

        if mode == "*": result = num1 * num2
        elif mode == "/": result = num1 / num2 if num2 != 0 else "Error: dividing by zero!"  
        elif mode == "+": result = num1 + num2
        elif mode == "-": result = num1 - num2
        elif mode == "exp": result = num1 ** num2
        else:  
            result = "Invalid mode!"
            print(result)
            continue  # Jump to next loop if valid.

        print("\nResult:", result)
        history.append(f"{num1} {mode} {num2} = {result}")

    # Continue?
    if input("\nContinue? (y/n): ").lower() != "y":
        print("\nHistory:", "\n".join(history))
        break
