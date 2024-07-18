## Errors and Exception Handling in Python

#### link:
https://www.youtube.com/watch?v=NIWwJbo-9_8
```md
## Errors and Exception Handling in Python 

This page equips you with the knowledge to identify, handle, and prevent errors in your Python programs. You’ll learn about common errors, exception handling mechanisms, and how to write robust code.


## Learning Objectives
 Differentiate between syntax errors and exceptions.
- Identify common Python exceptions and their causes.
- Utilize try, except, else, and finally blocks for exception handling.
- Raise exceptions with raise and create custom exceptions.
- Write code that anticipates and gracefully handles potential errors.


```

## Introduction
```md
Errors are inevitable in programming. Python errors can be broadly categorized into two main types:

`Syntax Errors: These errors occur when the code violates Python’s grammar rules. They are typically detected during the code compilation phase and prevent the program from running at all.

Exceptions: Exceptions are runtime errors that arise during program execution. They indicate unexpected situations that the program encounters. Exceptions allow you to write code that can gracefully handle these situations and prevent program crashes.


```
## Detailed Explanation 

```md
## Understanding Python Errors
## Common Syntax Errors

Missing colons (:) after statements
Incorrect indentation (Python relies on indentation for code blocks)
Unmatched parentheses or brackets
Typos in variable or function names

## Common Exceptions

- NameError: Occurs when a variable or function is used before it’s defined.

- TypeError: Raised when an operation is attempted on incompatible data types.

- IndexError: Thrown when trying to access an element outside the list or sequence’s index range.

- ZeroDivisionError: Occurs when attempting to divide by zero.

- ValueError: Indicates an inappropriate value passed to a function or operation.


```

## Mastering Exception Handling
Python provides a powerful mechanism called exception handling to manage errors. The fundamental structure involves try, except, else, and finally blocks:
```python
try:
  # Code that might raise an exception
except ExceptionType:
  # Code to handle the exception
else:
  # Code that executes if no exception occurs
finally:
  # Code that always executes, regardless of exceptions

```

```md
- try block: Contains the code that might potentially raise an exception.

- except block: Catches specific exceptions based on the ExceptionType. You can have multiple except blocks to handle different exception types.

- else block: Executes code only if no exceptions occur within the try block.

- finally block: Executes code regardless of whether an exception occurs or not. It’s commonly used for cleaning up resources like closing files.
```

```python
# You can also use the raise statement to explicitly raise an exception when encountering an error condition within your code:

def divide(x, y):
  if y == 0:
    raise ZeroDivisionError("Division by zero is not allowed")
  return x / y

```

## Custom Exceptions

```md
## What are Custom Exceptions?
Custom exceptions are user-defined exception classes that you create to handle specific errors or exceptional situations in your code.

By deriving custom exceptions from the base Exception class in Python, you can create more meaningful and specific error messages for your applications.

## Why Use Custom Exceptions?
- Specific Error Handling: Custom exceptions help in identifying and handling specific errors or situations unique to your application.

- Clarity and Readability: They provide clear and meaningful error messages, making your code more understandable and maintainable.

- Modularity: By encapsulating related error handling logic within custom exceptions, you can improve code modularity and organization.

```

## Creating Custom Exceptions


```md
## To create a custom exception:
- Define a new class that inherits from the base Exception class or its subclasses (e.g., ValueError, TypeError, etc.).

- Optionally, you can add custom attributes or methods to your exception class based on your requirements.

```

```python
## example 
class OutOfStockError(Exception):
    """Custom exception for handling out-of-stock items."""

    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock."

# Sample Product Inventory
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0,  # Out of stock
    "grapes": 3
}
```

## Break down
```md
## Let’s break down the provided code:

## Custom Exception OutOfStockError:

We define a custom exception class OutOfStockError that inherits from the base Exception class. 

This custom exception is designed to handle out-of-stock items.

The __init__ method initializes the exception with the name of the out-of-stock item.

The __str__ method specifies the error message to be displayed when the exception is raised.


## Sample Product Inventory:

We have a dictionary product_inventory that represents the available quantity of various items in our inventory.
Function purchase_item(item, quantity):

This function simulates purchasing items from the inventory.
It checks if the requested item is available in the inventory and if it’s in stock. If the item is in stock, it reduces the quantity accordingly.
If the item is out of stock, it raises the OutOfStockError custom exception



```

## Testing the Custom Exception
```python
def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            product_inventory[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")

# Testing the Custom Exception
try:
    purchase_item("apple", 3)  # Purchase successful
    purchase_item("orange", 1)  # Raises OutOfStockError
    purchase_item("watermelon", 1)  # Item not available
except OutOfStockError as e:
    print(e)  # Output:


# We use a try-except block to handle exceptions that may occur during the purchase process.

# We attempt to purchase items like “apple”, “orange”, and “watermelon” with different quantities.

# If an OutOfStockError is raised (due to an out-of-stock item), we catch it and print the custom error message using print(e).

```