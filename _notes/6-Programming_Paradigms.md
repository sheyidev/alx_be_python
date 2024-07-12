## Fundamentals of OOP in Python
```md

video link ======= https://www.youtube.com/watch?v=5JA5VmWfjC0&t=47s
This page introduces Object-Oriented Programming (OOP) concepts and their implementation in Python. 


You’ll explore the benefits of OOP and how it structures code for better maintainability and re-usability.

## Concept Overview
Topics:
Introduction to OOP Concepts
Getting Started with Python Classes and Objects

## Learning Objectives
- Understand the core principles of OOP: classes, objects, encapsulation, and abstraction.
- Be able to define classes and create objects in Python.
- Grasp the use of class attributes, instance methods, and the self keyword.

```
## Introduction 
```md 

## OOP
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects. 

It allows you to structure your code in a way that models real-world entities, making it easier to manage and maintain large-scale projects. 

Think of OOP as a way of writing code that mimics how things work in the real world. 

In real life, we deal with objects all the time—like cars, dogs, or phones. 

Each object has characteristics (like color, size, or brand) and things it can do (like drive, bark, or make calls).

 OOP lets us represent these objects and their actions in our code.
```

## Detailed Explanation 
```md
## Key Concepts in OOP:
Objects

Objects are like the things you see and interact with in everyday life (cars, dogs, etc.). Each object has properties (like color, size) and behaviors (like drive, bark).

Classes: A class is like a blueprint or template for creating objects. It defines what properties an object will have (attributes) and what actions it can perform (methods).

## Encapsulation:

Encapsulation means bundling data (attributes) and the methods (functions) that operate on that data together within a class. It helps keep related things together and hides the inner workings of an object from the outside, showing only what’s necessary.

## Inheritance:

Inheritance is like passing down traits from parent to child. It allows a new class (child) to inherit properties and behaviors from an existing class (parent), promoting code re-usability.

## Polymorphism: 
Polymorphism means many forms. It allows objects to take on different forms or behaviors based on the context or the class they belong to.

```

```python
## OOP sample 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default attribute value

    def get_descriptive_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
           self.odometer_reading += miles


## In this Car class:
"""
- We have an __init__ method (constructor) that initializes attributes like make, model,year, and odometer_reading.

- get_descriptive_name method returns a formatted string representing the car’s name.
- read_odometer method prints the car’s mileage.

- update_odometer method updates the odometer reading with a new value (if it’s higher). increment_odometer method increments the odometer reading by a specified amount.

"""
```

## Sample Question

```python
You can create object (instances) of the Car class and access its methods and attributes as follows:

my_car = Car("Toyota", "Camry", 2020)
print(my_car.get_descriptive_name())  # Output: 2020 Toyota Camry

my_car.read_odometer()  # Output: This car has 0 miles on it.
my_car.update_odometer(100)  # Update odometer reading
my_car.read_odometer()  # Output: This car has 100 miles on it.

my_car.increment_odometer(50)  # Increment odometer reading
my_car.read_odometer()  # Output: This car has 150 miles on it.

```

