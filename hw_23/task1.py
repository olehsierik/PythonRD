import unittest


def only_even(lst):
    even_list = filter(lambda x: x % 2 == 0, lst)
    return list(even_list)


class TestEven(unittest.TestCase):
    def test_only_even_empty_list(self):
        self.assertEqual(only_even([]), [])

    def test_only_even_valid(self):
        self.assertEqual(only_even([0, 1, 2, 3, 4]), [0, 2, 4])

    def test_only_even_negative_number(self):
        self.assertEqual(only_even([-1, -2, -3, -4]), [-2, -4])

    def test_only_even_add_number(self):
        self.assertEqual(only_even([1, 3, 5]), [])

    def test_only_even_tuple(self):
        self.assertEqual(only_even((1, 3, 5)), [])


if __name__ == "__main__":
    unittest.main()
