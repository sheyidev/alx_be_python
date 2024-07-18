## Objective: Implement a division calculator that
## robustly handles errors like division by zero and non-numeric inputs using command line arguments.
def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        if denominator == 0:
            raise ZeroDivisionError(f"Error: Cannot divide by zero")
        
        else:
            result = numerator /denominator
            print (f"The result of the division is {result:.1f}") 
    except:
        print("Error: Please enter numeric values only.")


    """
        if denominator == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    result = numerator / denominator
    return result
    #print(f"The result of the division is {result:.2f}")
     
    
    """


