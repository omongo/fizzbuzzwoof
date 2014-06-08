import unittest

from fizzbuzzwoof import FizzBuzzWoof

class TestFizzBuzzWoof(unittest.TestCase):

    def test_1_should_be_1(self):
        expected = '1'
        actual = FizzBuzzWoof().say(1)
        self.assertEqual(expected, actual)

    def test_3_should_be_Fizz(self):
        expected = 'Fizz'
        actual = FizzBuzzWoof().say(3)
        self.assertEqual(expected, actual)

    def test_5_should_be_Buzz(self):
        expected = 'Buzz'
        actual = FizzBuzzWoof().say(5)
        self.assertEqual(expected, actual)

    def test_7_should_be_Woof(self):
        expected = 'Woof'
        actual = FizzBuzzWoof().say(7)
        self.assertEqual(expected, actual)

    def test_15_should_be_FizzBuzz(self):
        expected = 'FizzBuzz'
        actual = FizzBuzzWoof().say(15)
        self.assertEqual(expected, actual)

    def test_21_should_be_FizzWoof(self):
        expected = 'FizzWoof'
        actual = FizzBuzzWoof().say(21)
        self.assertEqual(expected, actual)

    def test_35_should_be_BuzzWoof(self):
        expected = 'BuzzWoof'
        actual = FizzBuzzWoof().say(35)
        self.assertEqual(expected, actual)

    def test_105_should_be_FizzBuzzWoof(self):
        expected = 'FizzBuzzWoof'
        actual = FizzBuzzWoof().say(105)
        self.assertEqual(expected, actual)

