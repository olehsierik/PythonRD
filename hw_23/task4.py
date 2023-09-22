import pytest


def is_strong_password(string: str) -> bool:
    import re
    if (len(string) > 7 and
            re.search('[a-z]', string) and
            re.search('[A-Z]', string) and
            re.search('\d', string) and
            re.search('[^\w\s]', string)):
        return True
    return False



def test_strong_password():
    assert is_strong_password("Qwerty123!") == True
    assert is_strong_password("Password123!") == True


def test_short_password():
    assert is_strong_password("Qw1!") == False


def test_missing_uppercase():
    assert is_strong_password("password123!") == False


def test_missing_lowercase():
    assert is_strong_password("PASSWORD123!") == False


def test_missing_number():
    assert is_strong_password("Password!!") == False


def test_missing_special_character():
    assert is_strong_password("Password123") == False
