import unittest

from adder import add


class AdderTestCase(unittest.TestCase):

    def test_add_pos(self):
        self.assertEqual(add(1, 1), 2)

    def test_add_neg(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed(self):
        self.assertEqual(add(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
