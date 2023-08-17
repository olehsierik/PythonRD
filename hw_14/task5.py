def longest_word(file_name):
    import re

    try:
        with open(file_name, 'r') as file:
            content = file.read()
            content_list = sorted(re.split(r'(?<=[.!? ])', content), key=len, reverse=True)
            return content_list[0]
    except Exception:
        return

# print(longest_word('test'))

