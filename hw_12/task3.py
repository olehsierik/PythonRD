class MyManager:

    def __enter__(self):
        print('==========')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print('Exception is occured')
        print('==========')
        return True

# def divide(a, b):
#     return a / b


# with MyManager():
# res = divide(1, 0)
# print(f'The function call is successful, result is {res}')

# with MyManager():
#     res = divide(1, 1)
#     print(f'The function call is successful, result is {res}')
