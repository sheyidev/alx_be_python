## Inheritance and Polymorphism 

This page will delve into inheritance and polymorphism, two powerful concepts in object-oriented programming (OOP) that enhance code organization, re usability, and flexibility in Python.

## Concept Overview

```md
## Topics:
Mastering Inheritance
Polymorphism in Python

## Learning Objectives
Understand the concepts of inheritance and polymorphism.
Implement single, multiple, and multilevel inheritance in Python classes.
Explain method resolution order (MRO) in Python.
Utilize method overriding for polymorphism.
Leverage duck typing for polymorphic behavior
```

## Introduction
```md

Inheritance and polymorphism are fundamental pillars of OOP. Inheritance allows us to create new classes (child classes) that inherit properties and behaviors from existing classes (parent classes). Polymorphism enables objects of different classes to respond to the same method call in different ways.

```
```md
## Detailed Explanation

Mastering Inheritance
## Single Inheritance

 - A child class inherits from a single parent class.
 - The child class gains access to the attributes and methods of the parent class.

```

## Single Inheritance 
```python
class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

lassie = Dog("Lassie")
lassie.make_sound()  # Output: Woof!
```
## Multiple Inheritance 
- A child class inherits from multiple parent classes.
- Diamond problem (method ambiguity) can arise if parent classes have the same method.

## Multiple Inheritance
```python
class Flyer:
  def fly(self):
    print("Flying...")

class Swimmer:
  def swim(self):
    print("Swimming...")

class Duck(Flyer, Swimmer):
  pass

duck = Duck()
duck.fly()  # Output: Flying...
duck.swim()  # Output: Swimming...

```

## Multilevel Inheritance

A child class inherits from a parent class, which itself inherits from another parent class.
```python
class Vehicle:
  def move(self):
    print("Moving...")

class Car(Vehicle):
  pass

class ElectricCar(Car):
  def charge(self):
    print("Charging...")

tesla = ElectricCar()
tesla.move()  # Output: Moving...
tesla.charge()  # Output: Charging...

```
## Method Resolution Order (MRO)

What is Method Resolution Order (MRO)?

```md
## What is Method Resolution Order (MRO)?

Method Resolution Order (MRO) is the order in which Python searches for methods in classes during method calls, especially in cases of multiple inheritance (when a class inherits from more than one parent class).

 MRO helps Python determine which method to execute when there are method name conflicts or ambiguity due to inheritance.

## How does Python determine MRO?

Python uses the C3 Linearization algorithm to calculate the Method Resolution Order. 

It follows a depth-first left-to-right search pattern to maintain the order of inheritance and resolve method conflicts effectively.

Understanding MRO with an Example: Let’s consider a simple example with multiple inheritance to understand MRO better:

```

## MRO example 

```python
class A:
    def greet(self):
        return "Hello from class A"

class B(A):
    def greet(self):
        return "Hello from class B"

class C(A):
    def greet(self):
        return "Hello from class C"

class D(B, C):
    pass

# Creating an instance of class D
obj_d = D()
print(obj_d.greet())  # Output: "Hello from class B"
```
## Explanation

```md
## Let’s break it down:

Class D inherits from classes B and C, which in turn inherit from class A.

When we call obj_d.greet(), Python follows the MRO to determine which greet() method to execute.

The MRO for class D in this case is D -> B -> C -> A, following the depth-first left-to-right search.

Python finds the greet() method in class B first (left-most class in inheritance), so it executes the greet() method from class B.

Understanding MRO helps predict how Python resolves method calls in complex inheritance hierarchies.


It ensures that methods are executed in the expected order, maintaining the integrity of your program’s logic even with multiple levels of inheritance.
```
## Polymorphism in Python
```md
## Polymorphism in Python
What is Polymorphism?

Polymorphism is a fundamental concept in Object-Oriented Programming (OOP) that allows objects to take on different forms or behaviors based on their specific class or context.


 In simpler terms, it means that different objects can respond to the same method or function call in different ways. In this case, a child class redefines a method inherited from a parent class with its own implementation.

## Implementing Polymorphism and Method Overriding

Polymorphism is often achieved through method overriding, where a subclass provides a specific implementation of a method that it inherits from its superclass.

class Animal:
  def make_sound(self):
    print("Generic animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

animals = [Dog(), Animal()]
for animal in animals:
  animal.make_sound()  # Output: Woof! (for Dog), Generic animal sound (for Animal)
```
## Polymorphic Behavior with Duck Typing

Python uses a concept called “duck typing” to achieve polymorphic behavior. 

Duck typing emphasizes the object’s behavior over its type or class. It’s based on the idea that “if it looks like a duck and quacks like a duck, then it must be a duck.

```python
class Duck:
    def quack(self):
        return "Duck quacks"

class Person:
    def quack(self):
        return "Person imitates duck"

# Polymorphic behavior using duck typing
def make_sound(obj):
    return obj.quack()

duck_obj = Duck()
person_obj = Person()

print(make_sound(duck_obj))    # Output: "Duck quacks
print(make_sound(person_obj))  # Output: "Person imitates duck"

```
