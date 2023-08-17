def encrypt_caesar(filename, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = alphabet.upper()
    encrypted_alphabet = alphabet[offset:] + alphabet[:offset]
    encrypted_upper_alphabet = upper_alphabet[offset:] + upper_alphabet[:offset]
    mapping = {char: encrypted_char for char, encrypted_char in
               zip(alphabet + upper_alphabet, encrypted_alphabet + encrypted_upper_alphabet)}

    with open(filename, 'r+', encoding='utf-8') as file:
        content = file.read()
        encrypted_content = ''.join(mapping[char] if char in mapping else char for char in content)

        file.seek(0)
        file.write(encrypted_content)
        file.truncate()

    print(upper_alphabet)
    print('============================')
    print(encrypted_alphabet)
    print('============================')
    print(encrypted_upper_alphabet)
    print('============================')
    print(mapping)
# Приклад використання:
encrypt_caesar("test.txt", 3)
