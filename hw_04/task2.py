res = input("Enter some number: ")
if res.isnumeric():
    res = int(res)
    if res % 2 == 0:
        print(f"The number '{res}' is even")
    else:
        print(f"The number '{res}' is odd")
else:
    print(f"The value '{res}' is not a number")
