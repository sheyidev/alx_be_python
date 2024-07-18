## Testing Fundamentals in Python
```md
This page will introduce you to the importance of testing in software development and guide you through writing unit tests in Python using the unittest module.

## Topics:
The Role of Testing in Development Introduction to Writing Unit Tests




# Learning Objectives
Understand the significance of testing in the development process.

Be able to write basic unit tests for Python functions using the unittest module.

Grasp the concept of test cases and test runners.
```

## Introduction 

```md
Testing is a crucial part of software development that ensures the code functions as intended. It involves creating scenarios (test cases) to verify the correctness of different parts of your program.

By writing tests, you can:

- Catch bugs early: Tests help identify errors before they reach production, saving time and resources.

- Improve code quality: Writing tests encourages you to write clean, modular code that is easier to understand and maintain.

- Increase confidence in code changes: Tests provide a safety net when modifying code, ensuring existing functionalities aren’t broken.



```

## Detailed Explanation

```md
## The Role of Testing in Development
There are various types of testing in software development, each with a specific focus. Here, we’ll concentrate on unit testing. Unit testing involves testing individual units of code, typically functions or classes. It ensures that each unit performs its intended behavior with specific inputs.

## Writing Unit Tests
Python provides a built-in module called unittest for writing unit tests. Let’s explore its basic functionalities:

## Test Cases:
We define individual tests as test cases within a TestCase class. Each test case has a specific method named with test_ followed by a descriptive name. Inside this method, we write code to:

- Set up the test environment (e.g., create objects, initialize data).

- Execute the code we want to test (e.g., call the function with specific inputs).

Assert the expected outcome using self.assertEqual(actual, expected)

## Test Runners:
Once you’ve written your test cases, you need a test runner to execute them. The unittest module provides a TextTestRunner class that can be used to run all test cases within a test suite.
```

## Example(unittest)
https://www.youtube.com/watch?v=ULxMQ57engo&t=566s
```python
import unittest

def add(x, y):
  """Returns the sum of two numbers."""
  return x + y

class TestAdd(unittest.TestCase):

  def test_add_positive(self):
    result = add(5, 3)
    self.assertEqual(result, 8)

  def test_add_negative(self):
    result = add(-2, 7)
    self.assertEqual(result, 5)

if __name__ == "__main__":
  unittest.main()


## Check the coverage of tests covered 

pytest --cov

## optinonally
coverage html 
```