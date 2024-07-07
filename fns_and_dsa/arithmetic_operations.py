def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")


    match operation:
        case '+':
            result = num1 + num2
            print(f"Result: {result}")
        case "-":
            result = num1 - num2
            print(f"Result: {result}")
        case "*":
            result = num1 * num2
            print(f"Result: {result}")
        case "/":
            result = num1 / num2
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print(f"Result: {result}")
        case _:
            print("Invalid day entered.")
    