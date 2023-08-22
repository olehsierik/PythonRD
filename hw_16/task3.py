def is_strong_password(string: str) -> bool:
    import re
    if (len(password) > 7 and
            re.search('[a-z]', password) and
            re.search('[A-Z]', password) and
            re.search('\d', password) and
            re.search('[^\w\s]', password)):
        return True
    return False
