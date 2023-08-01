# my_text = 'THIS IS some Text. And this text, is just an EXAMPLE! trust me?'


def normalize_text(text: str):
    import re

    denormalize_list = re.split('([.!?])', my_text)
    normalized_list = []

    for item in denormalize_list:
        item = item.strip().capitalize()
        if item in ['.', '!', '?']:
            item += ' '
        normalized_list.append(item)

    normalized_text = ''.join(normalized_list)

    return normalized_text

# print(normalize_text(my_text))
