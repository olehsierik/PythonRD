while True:
    text = input('Enter some text: ')
    print(f'Entered text `{text}`')
    if text.lower().strip() == 'exit':
        break
