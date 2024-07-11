## Data Structures in Python 
This page will equip you with the fundamentals of Python data structures. You’ll learn about common data structures like lists, tuples, sets, and dictionaries, and understand when and why to use each one effectively in your programs.

## Topics
```md
## Topics
- Introduction to Python Data Structures
- Manipulating Data Structures ## Learning Objectives
- Understand the concept of data structures in Python.
- Identify the appropriate data structure for storing and organizing different types of data.
- Perform common operations on lists, tuples, sets, and dictionaries.
```

## Introduction

```md
## Introduction
Data structures are fundamental building blocks in Python that organize and store collections of data.Data structures are like containers that allow you to organize and store collections of data in a structured and efficient way. Think of them as different types of boxes or organizers where you can put your data items. Choosing the right data structure for your task is crucial for efficient code and memory usage.

## Here’s a brief overview of common data structures:

Lists: Ordered, mutable collections of items enclosed in square brackets []. They can hold elements of different data types and allow duplicate values.

Tuples: Ordered, immutable collections of items similar to lists but enclosed in parentheses (). Once created, their elements cannot be changed.

Sets: Unordered collections of unique elements enclosed in curly braces {}. Sets are useful for removing duplicates and checking element membership.

Dictionaries: Unordered collections of key-value pairs enclosed in curly braces {}. Keys must be unique and immutable, while values can be of any data type. Dictionaries are efficient for storing data associated with labels.

```

## Manipulating Data Structures
```md
## Operations on Lists
Indexing:

- What it is: Indexing is the process of accessing elements in a list by their position.
- How it works: In Python, indexing starts from 0 for the first element, 1 for the second, and so on. You can use square brackets [] with the index number to access the element at that position.
- Example: If you have a list my_list = [10, 20, 30, 40, 50], my_list[0] would give you 10, my_list[2] would give you 30, and so on.
 

Slicing:
What it is: Slicing allows you to extract sub-lists from a list using start, stop, and step indices.

How it works: You use the syntax list[start:stop:step] to slice a list. The start index is inclusive, the stop index is exclusive, and step is the interval between elements.

Example: Using our previous list, my_list[1:4] would give [20, 30, 40], my_list[::2] would give [10, 30, 50] (step of 2), and my_list[::-1] would reverse the list.


Appending:
What it is: Appending is adding elements to the end of a list.
How it works: You use the append() method to add an element to the end of the list.
Example: Continuing with our list, if you do my_list.append(60), the list becomes [10, 20, 30, 40, 50, 60]

Removing
What it is: Removing is deleting elements from a list.
How it works: You can use the remove() method to delete a specific element by its value or use the del keyword followed by the index to delete by index.
Example: If you do my_list.remove(30), it removes 30 from the list. If you do del my_list[0], it deletes the element at index 0 (10 in this case).
```
## Exploring Dictionary Methods, Tuple Immutability, and Set Operations
```md

Exploring Dictionary Methods

Dictionaries provide methods like get(key, default), keys(), values(), and items() for accessing and manipulating key-value pairs.

get(key, default): This method retrieves the value associated with a specified key in the dictionary. If the key is not found, it returns the default value (if provided) or None.

keys(): This method returns a view object that contains all the keys in the dictionary, allowing you to iterate over them

values(): Similar to keys(), this method returns a view object that contains all the values in the dictionary.

items(): This method returns a view object that contains tuples of key-value pairs, allowing you to iterate over them together.

## Tuple Immutability

Tuples are like lists, but once they are created, you cannot change their elements. This property is called immutability.

Immutability ensures that the contents of a tuple remain constant, which can be useful in situations where you don’t want accidental changes to data.
However, you can still access elements in a tuple using indexing or slicing, just like lists.


## Set

Sets are collections of unique elements, meaning they don’t allow duplicate values. Sets offer operations like union, intersection, and difference for combining and comparing sets.

union(): Combines two sets to create a new set containing all unique elements from both sets.
intersection(): Finds the common elements between two sets.
difference(): Finds the elements present in one set but not in another set.
```
