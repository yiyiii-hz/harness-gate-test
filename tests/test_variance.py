import unittest

from stats import variance


class VarianceTest(unittest.TestCase):
    def test_population_variance(self):
        self.assertAlmostEqual(variance([2, 4, 4, 4, 5, 5, 7, 9]), 4.0)

    def test_simple(self):
        self.assertAlmostEqual(variance([1, 2, 3, 4]), 1.25)

    def test_single_value(self):
        self.assertEqual(variance([5]), 0)

    def test_constant_values(self):
        self.assertEqual(variance([3, 3, 3]), 0)

    def test_floats(self):
        self.assertAlmostEqual(variance([0.5, 1.5]), 0.25)

    def test_empty(self):
        with self.assertRaises(ValueError):
            variance([])


if __name__ == "__main__":
    unittest.main()
