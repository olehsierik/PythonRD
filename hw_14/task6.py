def encrypt_ceaser(file_name, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    alphabet_dict = {}

    for letter in alphabet:
        alphabet_dict[letter] = alphabet[(alphabet.index(letter) + offset) % len(alphabet)]

    with open(file_name, 'r+') as file:
        content = file.read()

        encrypt_content = ''
        for item in content:
            if item.isalpha() and item.islower():
                encrypt_content = encrypt_content + alphabet_dict[item]
            elif item.isalpha() and item.isupper():
                encrypt_content = encrypt_content + alphabet_dict[item.lower()].upper()
            else:
                encrypt_content = encrypt_content + item

        file.seek(0)

        file.write(encrypt_content)
