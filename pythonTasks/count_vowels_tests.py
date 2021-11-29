import count_vowels
import unittest


class CountVowelsTests(unittest.TestCase):

    def test_get_res(self):
        self.res = count_vowels.get_res('robocop obama UNDERGROUND 2')
        self.assertEqual(self.res, 10)


if __name__ == '__main__':
    unittest.main
