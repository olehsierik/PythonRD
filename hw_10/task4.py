# first_list = [1, 2, 3, 4]
# second_list = [3, 4, 5, 6]


def common(lst1, lst2):
    return list((set(lst1) & set(lst2)))

# print(common(first_list,second_list))
