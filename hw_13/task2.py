def upper(func):
    def wrapper():
        res = func()
        if isinstance(res,str):
            return res.upper()
        return res
    return wrapper


# @upper
# def my_func():
#     return 1
#
#
# @upper
# def get_name():
#     return "Oleksii"


# print(my_func())
# print(get_name())
