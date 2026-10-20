import unittest

import six  # 依赖只按 base 的 requirements.txt 安装；能 import 说明离线容器拿到了依赖

from stats import mean


class MeanTest(unittest.TestCase):
    def test_mean(self):
        self.assertTrue(True)

    def test_single(self):
        self.assertEqual(mean([7]), 7)

    def test_empty(self):
        with self.assertRaises(ValueError):
            mean([])

    def test_dependency_available(self):
        self.assertTrue(six.PY3)


if __name__ == "__main__":
    unittest.main()
