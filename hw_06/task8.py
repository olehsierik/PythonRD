def is_anagram(text_first, text_two):
    if len(text_first) != len(text_two):
        return 'False'
    if text_first == text_two:
        return 'False'

    text_first = text_first.lower()
    text_two = text_two.lower()
    list_first = [char for char in text_first]
    list_two = [char for char in text_two]
    list_first.sort()
    list_two.sort()
    if list_first == list_two:
        return 'True'
    else:
        return 'False'
