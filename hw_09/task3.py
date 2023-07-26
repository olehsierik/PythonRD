# my_list = [0, 1, 2, 3, 4, 5, 6, 9, 78]


def add_to_list_index(lst, value, index=None):
    if index is None:
        lst.append(value)
    else:
        lst.insert(index, value)


# add_to_list_index(my_list, 99)

# print(my_list)
