def operate(x, y, operation):
    return {
        '1': lambda: x + y,
        '2': lambda: x - y,
        '3': lambda: x * y,
        '4': lambda: "Error: Cannot divide by zero." if y == 0 else x / y,
    }.get(operation, lambda: "Invalid operation")()

def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} {['+', '-', '*', '/'][int(choice) - 1]} {num2} =", operate(num1, num2, choice))
    else:
        print("Invalid input. Please enter a valid choice.")

# Run the calculator
calculator()
