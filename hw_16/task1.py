def validate_phone(phone_number: str) -> bool:
    import re

    phone_number_pattern = re.compile("\+380\d{9}$|^380\d{9}$|^0\d{9}$")

    return bool(phone_number_pattern.search(phone_number))
