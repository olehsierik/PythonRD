def init():
    return {}


def add_to_dict(dct: dict, key, value):
    dct[key] = value


def remove_from_dict(dct: dict, key):
    dct.pop(key,None)


def value_by_key(dct: dict, key):
    return dct.get(key)


def list_of_key(dct: dict):
    return list(dct.keys())


def key_exist(dct: dict, key):
    return key in dct


def main():
    phone_book = init()

    while True:

        command = input('Enter command: ')
        if command.lower().strip() == 'add':
            name = input('Enter name: ')
            if key_exist(phone_book, name):
                print('Name already exists')
            else:
                phone_number = input('Enter phone number: ')
                add_to_dict(phone_book, name, phone_number)
        elif command.lower().strip() == 'remove':
            name = input('Enter name for remove: ')
            remove_from_dict(phone_book, name)
        elif command.lower().strip() == 'list':
            print(list_of_key(phone_book))
        elif command.lower().strip() == 'show':
            name = input('Enter search name: ')
            if value_by_key(phone_book, name):
                print(value_by_key(phone_book, name))
            else:
                print('Name not found')
        elif command.lower().strip() == 'exit':
            break
        else:
            print('''List of command:
                    add - add contact
                    remove - delete a contact
                    list - show contact list
                    show - show contact number
                    exit - close the program''')


if __name__ == "__main__":
    main()
