res = input("Enter something: ")
if res.isnumeric():
    print(f"Entered value '{res}' is a number")
else:
    print(f"Entered value '{res}' is a text")
