def copy(file_name):
    file_name_lst = file_name.split('.')
    file_name_lst[0] = file_name_lst[0] + '_copy'
    new_file_name = '.'.join(file_name_lst)

    with open(file_name, 'r') as file:
        content = file.read()
    with open(new_file_name, 'w+') as new_file:
        new_file.write(content)

# copy('test.txt')
