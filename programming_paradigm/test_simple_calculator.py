## Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator
## class that supports addition, subtraction, multiplication, and division operations.
# simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestAdd(unittest.TestCase):
    def test_addition(self):
        result = SimpleCalculator()
        result = result.add(2, 4)
        self.assertEqual(result, 6)


