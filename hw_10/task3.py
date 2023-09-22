my_list = ['this', '   IS ', 'a', '  TEST OF THE FUNCTION   ']

def normalize(lst: list):
    normalize_list = map(lambda x: x.strip().capitalize(), lst)
    return list(normalize_list)

print(normalize(my_list))