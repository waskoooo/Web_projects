def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


while True:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    operation = input("Choose operation (+, -, *, /): ")

    if operation == '+':
        print(add(x, y))
    elif operation == '-':
        print(subtract(x, y))
    elif operation == '*':
        print(multiply(x, y))
    elif operation == '/':
        print(divide(x, y))
    else:
        print("Invalid operation")

    another = input("Do you want to do another operation? (yes/no): ")
    if another.lower() != 'yes':
        break
