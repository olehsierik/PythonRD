def no_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            print(exc)
    return wrapper


# @no_exception
# def divide(a, b):
#     return a / b
#
#
# print(divide(1, 0))
# print('===')
# print(divide(1, 1))
