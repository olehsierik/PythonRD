# my_list = [1,2,3,4,5,6,7]

def only_even(lst):
    even_list = filter(lambda x: x % 2 == 0, lst)
    return list(even_list)

# print(only_even(my_list))