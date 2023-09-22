import unittest


def normalize(lst: list) -> list:
    if not isinstance(lst, list):
        raise TypeError
    normalize_list = map(lambda x: x.strip().capitalize(), lst)
    return list(normalize_list)


class TestNormalize(unittest.TestCase):
    def test_normalize(self):
        test_list: list = ['this', '   IS ', 'a', '  TEST OF THE FUNCTION   ']
        res_list: list = ['This', 'Is', 'A', 'Test of the function']
        self.assertEqual(normalize(test_list), res_list)

    def test_normalize_not_list(self):
        with self.assertRaises(TypeError):
            normalize("This is not a list")


if __name__ == "__main__":
    unittest.main()
