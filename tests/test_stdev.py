import math
import unittest

from stats import stdev, variance


class StdevTest(unittest.TestCase):
    def test_population_stdev(self):
        self.assertAlmostEqual(stdev([2, 4, 4, 4, 5, 5, 7, 9]), 2.0)

    def test_is_sqrt_of_variance(self):
        values = [1.5, 2.5, 3.5, 10.0]
        self.assertAlmostEqual(stdev(values), math.sqrt(variance(values)))

    def test_single_value(self):
        self.assertEqual(stdev([42]), 0)

    def test_constant_values(self):
        self.assertEqual(stdev([3, 3, 3]), 0)

    def test_empty(self):
        with self.assertRaises(ValueError):
            stdev([])


if __name__ == "__main__":
    unittest.main()
