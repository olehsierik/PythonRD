def repeat(n):
    def my_deco(func):
        def wrapper():
            for _ in range(n):
                res = func()
            return res

        return wrapper

    return my_deco


# @repeat(3)
# def my_func():
#     print("test")
#
#
# @repeat(5)
# def my_another_func():
#     return 1
#
#
# my_func()
# print(my_another_func())
