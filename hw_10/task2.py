# my_list = [1,1,3,1,5,1,7]

def only_even(lst: list):
    even_list = filter(lambda x: x % 2 == 0, lst)
    return list(even_list)

print(only_even((1,2,3,4)))