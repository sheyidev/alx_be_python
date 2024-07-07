def perform_operation(num1, num2):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("choose the operation (+, -, *, /): ")


    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}")
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
        case "/":
            result = num1 / num2
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print(f"The result is {result}")
        case _:
            print("Invalid day entered.")
    
