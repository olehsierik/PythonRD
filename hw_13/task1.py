from datetime import datetime


def simple_decorator(func):
    def wrapper():
        print(datetime.now().isoformat())
        return func()

    return wrapper


# @simple_decorator
# def my_func():
#     return 1
#
#
# res = my_func()
# print(res)
