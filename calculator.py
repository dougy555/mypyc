# A simple Python program to perform basic arithmetic operations.

def calculator():
    """
    This function prompts the user for two numbers and a mathematical
    operation, then performs the calculation and prints the result.
    """
    # Ask the user to input the first number and convert it to a float.
    # Using a try-except block to handle cases where the user inputs non-numeric data.
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter a mathematical operation (+, -, *, /): ")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Perform the calculation based on the user's input.
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        # Handle the special case of division by zero.
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        # If the user enters an invalid operation.
        print("Invalid operation. Please use +, -, *, or /.")

# Run the calculator function.
calculator()