import unittest

from stats import mode


class ModeTest(unittest.TestCase):
    def test_mode(self):
        self.assertEqual(mode([1, 2, 2, 3]), 2)

    def test_tie(self):
        self.assertEqual(mode([3, 1, 3, 1]), 1)

    def test_empty(self):
        with self.assertRaises(ValueError):
            mode([])
