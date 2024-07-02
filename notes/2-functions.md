## Understanding Functions in Python

```md
## Introduction

This is an introduction to functions, a fundamental building block in Python programming. 
You’ll understand how functions help organize code, improve readability, and promote re-usability.


## functions 

Functions are reusable blocks of code that perform specific tasks. They allow you to break down complex programs into smaller, manageable parts. By using functions, you can:

Improve code readability and maintainability.
Make code more modular and reusable.
Avoid code duplication.
```
## lambda functions
```md
## Lambda Functions
Python also supports lambda functions, which are used for writing simple, one-line expressions. They are also known as anonymous functions because they don’t need a name to be defined. 

Lambda functions are especially useful when you need to pass a simple function as an argument to another function, like in the map(), filter(), or reduce() functions.

They are also commonly used in situations where a small, temporary function is needed without defining a full function separately. However, they are limited to single expressions and cannot contain multiple lines of code or complex logic.




add = lambda x, y: x + y
result = add(5, 3)  
print(result)  # Output: 8
```
## Function Parameters and Return Values

```md
## Function Parameters and Return Values
Function parameters are variables defined in the function’s declaration. They receive values when the function is called and are used within the function’s code block.



## Types of Parameters
- Positional Parameters: Parameters passed based on their position in the function call.
- Keyword Parameters: Parameters passed with their corresponding variable names.
- Default Parameters: Parameters with predefined default values.
- Variable-length Parameters: Parameters that can accept a variable number of arguments.

def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    return area
```

## Argument Passing
```md
## Argument Passing
When you call or use a function, you provide actual values or data that fit into those parameter placeholders. These actual values are called arguments.

# Passing argument
calculate_area(10, 5)  # rectangle_area will be 50
```
## Keyword Arguments 

```md
## Keyword Arguments
When we talk about “passing arguments by name using keyword arguments,” we are referring to a way of giving values to functions. Now, let’s talk about keyword arguments. 

Instead of relying on the position of arguments, you can explicitly specify which parameter should take which value by using keywords (parameter names) when calling the function. 


This approach can be helpful when dealing with functions that have many parameters, as it makes the code more readable and less error-prone by explicitly stating what each value represents.

def user_info(name, age=None):
     """Prints user information."""
    print(f"Name: {name}")
    if age:
    print(f"Age: {age}")
## calling the function 
user_info(name="Bob", age=30)
```
## Return Values 

```md
## Return values 
Return values are the values that a function sends back to the caller after execution. They are specified using the return statement in Python. Python functions can return multiple values as a tuple or other iterable types.


def square(number):
 """Returns the square of a number."""
 return number * number
squared_value = square(4)  # squared_value will be 16
```

## Variable Scope and Functions 

```md
## local vs Global scope 

Variables defined within a function have a local scope, meaning they are only accessible within the function body. Variables defined outside functions have a global scope, accessible throughout the program.

count = 0  # Global variable
def increment():
     count += 1  # This refers to the local count within the function
    increment()
print(count)  # Output: 0 (Global count remains unchanged)
```
## global and nonlocal Keywords
```md
## Use the global keyword to modify a global variable from within a function
count = 0
def increment_global():
  global count
  count += 1
increment_global()
print(count)  # Output: 1 (Global count is modified)
```
## nonlocal keyword

```md
## using the nonlocal keyword

Use the nonlocal keyword to modify a variable from an enclosing function within a nested function. Let’s break down the concept of using the nonlocal keyword to modify a variable from an enclosing function within a nested function in simpler terms. 
First, let’s understand what nested functions and enclosing functions are: *Nested Function: This is a function defined within another function. 


*Enclosing Function: This is the outer function that contains the nested function. Now, when you have a nested function inside an enclosing function, by default, the nested function can access variables from the enclosing function, but it cannot modify them directly. However, using the nonlocal keyword allows us to modify these variables indirectly.

## example 
def outer_function():
    x = 10  # Variable in the enclosing function

    def inner_function():
        nonlocal x  # Using nonlocal to modify x from the enclosing function
        x += 5  # Modifying the value of x

    inner_function()  # Calling the nested function
    print("Modified value of x from inner function:", x)
        outer_function()
```
