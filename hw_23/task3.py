import unittest
import random
import string


def validate_phone(phone_number: str) -> bool:
    import re

    phone_number_pattern = re.compile("\+380\d{9}$|^380\d{9}$|^0\d{9}$")

    return bool(phone_number_pattern.search(phone_number))


class TestValidPhone(unittest.TestCase):
    def test_valid_phone(self):
        self.assertEqual(validate_phone('+380673494349'), True)
        self.assertEqual(validate_phone('380673494349'), True)
        self.assertEqual(validate_phone('0673494349'), True)

    def test_validate_short_phone_number(self):
        self.assertEqual(validate_phone(f'+380{"".join(random.choices(string.digits, k=random.randint(1, 8)))}'), False)
        self.assertEqual(validate_phone(f'380{"".join(random.choices(string.digits, k=random.randint(1, 8)))}'),
                         False)
        self.assertEqual(validate_phone(f'0{"".join(random.choices(string.digits, k=random.randint(1, 8)))}'), False)

    def test_validate_short_long_number(self):
        self.assertEqual(validate_phone(f'+380{"".join(random.choices(string.digits, k=random.randint(10, 90)))}'),
                         False)
        self.assertEqual(validate_phone(f'380{"".join(random.choices(string.digits, k=random.randint(10, 90)))}'),
                         False)
        self.assertEqual(validate_phone(f'0{"".join(random.choices(string.digits, k=random.randint(10, 90)))}'), False)

    def test_random_number(self):
        self.assertEqual(validate_phone("".join(random.choices(string.digits, k=random.randint(1, 90)))), False)

    def test_validate_phone_number_special_character(self):
        self.assertEqual(validate_phone('!380673494349'), False)
        self.assertEqual(validate_phone('+A80673494349'), False)


if __name__ == "__main__":
    unittest.main()
