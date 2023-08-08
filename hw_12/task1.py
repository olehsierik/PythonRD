def handle_exception(func, *args, **kwargs):
    print('==========')
    try:
        func(*args, **kwargs)
    except Exception:
        print('Exception is occured')
    else:
        print('The function call is successful')
    finally:
        print('==========')


# def my_func(a, b):
#     a / b


# handle_exception(my_func, 1, 1)

