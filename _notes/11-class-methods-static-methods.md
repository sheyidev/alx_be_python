## More on Class Methods and Static Methods

```md

This page will guide you through understanding class methods and static methods in Python. 

You’ll learn the key differences between them, how to use @classmethod and @staticmethod decorators, and explore practical use cases for each.

## Concept Overview
## Topics:
Introduction to Class Methods and Static Methods
Using @classmethod Decorator
Using @staticmethod Decorator


## Learning Objectives
Understand the concepts of class methods and static methods in Python.

Differentiate between class methods and static methods based on their behavior and relationship with the class.

Effectively use @classmethod and @staticmethod decorators to define these methods in your classes.

```

## Introduction

```md
## Introduction
In object-oriented programming (OOP), classes serve as blueprints for creating objects. Methods are functions defined within a class that operate on objects of that class. However, Python offers special methods that have a different relationship with the class itself: class methods and static methods.


## Detailed Explanation
## Introduction to Class Methods and Static Methods


## Class Methods

Class methods are methods that are bound to the class itself rather than instances of the class (objects). 

They are used to define methods that operate on class-level data or perform operations related to the class. They are defined using the @classmethod decorator, and the first parameter conventionally named cls represents the class itself.

## When to Use Class Methods
When you need to access or modify class-specific variables or properties.

When you want to create factory methods to create instances of the class with specific configurations.
```

## Example class methods 

```python
class Person:
    count = 0  # Class variable to count instances

    def __init__(self, name):
        self.name = name
        Person.count += 1  # Increment count on instance creation

    @classmethod
    def display_count(cls):
        print(f"Total persons created: {cls.count}")

# Usage
person1 = Person("Alice")
person2 = Person("Bob")
Person.display_count()  # Output: Total persons created: 2

```
## Breaking down 
```md
## Class Definition:

Defines a class named Person to represent individuals.
Has a class variable count initialized to 0, which will count the number of instances created from this class.


Includes an __init__ method (constructor) that takes a name parameter to initialize the name attribute for each person object.


Increments the count class variable by 1 every time a new instance of Person is created, using Person.count += 1 within the constructor.


## Class Method (display_count):

Defines a class method display_count using the @classmethod decorator.

Class methods take the class itself cls as the first parameter instead of the instance (self).

Prints the total number of persons created by accessing the count class variable.

## Creating Person Instances:

Creates two instances of the Person class named person1 and person2 with names “Alice” and “Bob”, respectively.


## Using the Class Method:

Calls the display_count class method using Person.display_count() to print the total number of persons created.


## Static Methods
Static methods are independent of class instances and the class itself. They behave like regular functions but are defined inside a class for organization purposes. They are defined using the @staticmethod decorator and don’t require the self or cls parameter.

## When to Use Static Methods
- When a method doesn’t need access to class or instance variables (attributes).
- When you want to group utility functions related to the class within the class definition.
```

## Example

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Usage
print(MathUtils.add(5, 3))       # Output: 8
print(MathUtils.multiply(5, 3))  # Output: 15

```

```md
This code defines a class MathUtils with two static methods:add and multiply. Static Methods:

add(a, b) method takes two arguments a and b and returns their sum.

multiply(a, b) method takes two arguments a and b and returns their product

MathUtils.add(5, 3) calls the static method add with arguments 5 and 3, returning the sum 8.


MathUtils.multiply(5, 3) calls the static method multiply with arguments 5 and 3, returning the product 15.


In the provided code, MathUtils acts as a utility class for basic arithmetic operations, demonstrating the use of static methods for encapsulating related functionality within a class without the need for instance variables or methods.

```

## Example from youtube 
link1 - https://www.youtube.com/watch?v=upmOAPk2cK8&t=451s

link2 - 


![static_method](https://github.com/sheyijojo/Docker_CERT/blob/main/_assets/static.png?raw=true)

![static_method](https://github.com/sheyijojo/Docker_CERT/blob/main/_assets/replica_set_demo.png?raw=true)
```md


```
