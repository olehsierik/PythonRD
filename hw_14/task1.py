def word_count(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        print(len(data.split(' ')))

# word_count('test')
