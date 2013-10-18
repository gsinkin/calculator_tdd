import unittest
import calculator


class TestCalculatorAddition(unittest.TestCase):

    def setUp(self):
        # setUp is run at the start of every test. It creates a Calculator
        # instance and makes it a member of the test instance (which
        # allows us to reference the calculator using self.calculator)
        self.calculator = calculator.Calculator()

    def test_addition_identity(self):
        self.assertEquals(1, self.calculator.add(1, 0))
        self.assertEquals(1, self.calculator.add(0, 1))
        self.assertEquals(-1, self.calculator.add(-1, 0))
        self.assertEquals(-1, self.calculator.add(0, -1))

    def test_addition_of_negatives(self):
        self.assertEquals(1, self.calculator.add(2, -1))
        self.assertEquals(1, self.calculator.add(-1, 2))
        self.assertEquals(-1, self.calculator.add(-2, 1))
        self.assertEquals(-1, self.calculator.add(1, -2))

    # ...and so on. Python unittest has a bunch of great built in features

if __name__ == '__main__':
    # these lines allow us to run this file like so: python addition_tests.py
    unittest.main()
