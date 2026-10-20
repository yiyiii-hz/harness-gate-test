import unittest

from stats import range_


class RangeTest(unittest.TestCase):
    def test_normal_values(self):
        self.assertEqual(range_([3, 1, 4, 1, 5, 9, 2, 6]), 8)

    def test_negative_and_float_values(self):
        self.assertAlmostEqual(range_([-2.5, 0.0, 1.5]), 4.0)

    def test_unsorted_input_not_modified(self):
        values = [5, 2, 8]
        self.assertEqual(range_(values), 6)
        self.assertEqual(values, [5, 2, 8])

    def test_single_value(self):
        self.assertEqual(range_([42]), 0)

    def test_empty(self):
        with self.assertRaises(ValueError) as ctx:
            range_([])
        self.assertEqual(str(ctx.exception), "values must not be empty")


if __name__ == "__main__":
    unittest.main()
