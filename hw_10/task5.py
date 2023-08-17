my_text = 'THIS IS some Text. And this text, is just an EXAMPLE! trust me'


def normalize_text(text):
    import re

    denormalize_list = re.split(r'(?<=[.!? ])', text)
    normalized_list = [item.strip().capitalize() for item in denormalize_list]
    print(normalized_list)
    print()

    if normalized_list[-1] == '':
            normalized_text = ' '.join(normalized_list)[:-1]
    else:
        normalized_text = ' '.join(normalized_list)

    return normalized_text


print(normalize_text(my_text))
