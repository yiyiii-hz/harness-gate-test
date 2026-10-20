import unittest

from stats import median


class MedianExtra(unittest.TestCase):
    def test_wrong_expectation(self):
        self.assertEqual(median([1, 2, 3, 4]), 3)
