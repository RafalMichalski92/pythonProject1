import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Testy dodawania
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -4), -6)

    def test_add_positive_and_negative(self):
        self.assertEqual(self.calc.add(5, -3), 2)

    # Testy odejmowania
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtract_positive_and_negative(self):
        self.assertEqual(self.calc.subtract(5, -3), 8)

    # Testy mnożenia
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(self.calc.multiply(3, -3), -9)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(3, 0), 0)

    # Testy dzielenia
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-6, -2), 3)

    def test_divide_positive_and_negative(self):
        self.assertEqual(self.calc.divide(6, -3), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

# Uruchomienie testów
if __name__ == '__main__':
    unittest.main()