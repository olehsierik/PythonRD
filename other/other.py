def divide(a: int, b: int) -> int:
    div: int = 0
    while a >= b:
        a -= b
        div += 1
    return div


print(divide(9, 9))
