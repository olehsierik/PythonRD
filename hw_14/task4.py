def logger(func):
    def wrapper():
        func_name = func.__name__
        with open('calls.log', 'a') as file:
            file.write(func_name + '\n')
        return func()

    return wrapper


# @logger
# def div():
#     return 1 / 5
#
#
# div()
