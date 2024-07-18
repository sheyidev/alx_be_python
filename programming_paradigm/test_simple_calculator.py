## Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator
## class that supports addition, subtraction, multiplication, and division operations.
# simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestAdd(unittest.TestCase):
    def test_addition(self):
        self.calc = SimpleCalculator()
        #result = self.calc.add(2, 4)
        self.assertEqual(self.calc.add(2, 4), 6)
    def test_subtraction(self):
        self.calc = SimpleCalculator()
    
        self.assertEqual(self.calc.subtract(4, 2), 2)
    def test_multiplication(self):
        self.calc = SimpleCalculator()

        self.assertEqual(self.calc.multiply(4, 2), 8)
    def test_division(self):
        self.calc = SimpleCalculator()

        self.assertEqual(self.calc.divide(10, 5), 2)
if __name__ == "__main__":
    unittest.main()
