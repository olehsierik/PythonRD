def is_anagram(text_first, text_two):
    if len(text_first) != len(text_two):
        return False
    if text_first == text_two:
        return False

    sorted_text1 = sorted(text_first)
    sorted_text2 = sorted(text_two)

    if sorted_text1 == sorted_text2:
        return True
    else:
        return False
