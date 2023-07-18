def power(number):
    return pow(number, 2)


def apply(value, modifier):
    return modifier(value)


res = apply(12, power)
print(res)


# ================ option 2 ================ #


def apply_2(value, func):
    return func(value)


result1 = apply(5, lambda x: x ** 2)
print(result1)
