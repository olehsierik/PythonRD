# my_list = [3, 1, 3 , 1]


def is_palindromic(lst):
    inverse_list = lst[::-1]
    if inverse_list == lst:
        return True
    else:
        return False

# print(my_list)
# print(my_list[::-1])
#
# print(is_palindromic(my_list))
