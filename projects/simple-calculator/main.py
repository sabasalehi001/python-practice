def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def get_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation_input():
    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in ('+', '-', '*', '/'):
            return operation
        else:
            print("Invalid operation. Please enter +, -, *, or /.")

if __name__ == "__main__":
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")
    operation = get_operation_input()

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        result = "Invalid operation"

    print("Result:", result)
