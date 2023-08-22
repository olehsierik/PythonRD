# def words_count(file_name):
#     with open(file_name, 'r') as file:
#         data = file.read()
#         print(data.split(' '))
#         print(len(data.split(' ')))

def words_count(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        return len(data.split(' '))

# def words_count(file_name):
#     with open(file_name, 'r') as file:
#         data = file.readlines()
#         data = ' '.join(data)
#         return len(data.split(' '))


print(words_count('test'))
