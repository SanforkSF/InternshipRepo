import fizz_buzz
import unittest


class FizzBuzzTests(unittest.TestCase):
    def test_get_reply_fizzbuzz(self):
        self.res = fizz_buzz.get_reply(15)
        self.assertEqual(self.res, 'FizzBuzz')

    def test_get_reply_fizz(self):
        self.res = fizz_buzz.get_reply(18)
        self.assertEqual(self.res, 'Fizz')

    def test_get_reply_buzz(self):
        self.res = fizz_buzz.get_reply(40)
        self.assertEqual(self.res, 'Buzz')

    def test_get_reply_other(self):
        self.res = fizz_buzz.get_reply(8)
        self.assertEqual(self.res, '')


if __name__ == '__main__':
    unittest.main
