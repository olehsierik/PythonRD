# my_list = [1, 2, 3, 3, 4, 4]


def unique(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


# print(my_list)

# print(unique(my_list))
