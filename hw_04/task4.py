res = input("Enter something: ")
if res.isnumeric():
    res = int(res)
    if res % 2 == 0:
        print(f"Entered value '{res}' is an even number")
    else:
        print(f"Entered value '{res}' is an odd number")
else:
    print(f"Entered value '{res}' is a text with length {len(res)}")
