import calculator
import unittest


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.res = calculator.Calculator().add(14.7, 2.5)
        self.assertEqual(self.res, 17.2)

    def test_subtract(self):
        self.res = calculator.Calculator().subtract(15, 2)
        self.assertEqual(self.res, 13)

    def test_multiply(self):
        self.res = calculator.Calculator().multiply(7, 4)
        self.assertEqual(self.res, 28)

    def test_divide(self):
        self.res = calculator.Calculator().divide(12, 4)
        self.assertEqual(self.res, 3.0)

    def test_zero_divide(self):
        self.res = calculator.Calculator().divide(12, 0)
        self.assertEqual(self.res, 'Zero division')


if __name__ == '__main__':
    unittest.main
