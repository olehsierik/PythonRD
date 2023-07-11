text = input("Enter some text: ")

for symbol in text:
    if symbol.isdigit():
        if int(symbol) % 2 == 0:
            print(f"The symbol `{symbol}` is an even digit")
        else:
            print(f"The symbol `{symbol}` is an odd digit")
    elif symbol.isalpha():
        if symbol.isupper():
            print(f"The symbol `{symbol}` is an uppercase letter")
        else:
            print(f"The symbol `{symbol}` is an lowercase letter")
    else:
        print(f"The symbol `{symbol}` is neither a digit not or letter")