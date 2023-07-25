# my_tuple = (1, 2, 3)


def add_to_tuple(tpl: tuple, value):
    tuple_to_list = list(tpl)
    tuple_to_list.append(value)
    return tuple(tuple_to_list)

# print(add_to_tuple(my_tuple, 10))
