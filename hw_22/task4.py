class MyInt(int):

    def __getitem__(self, item):
        my_int_str: str = str(self)
        return my_int_str[item]


n = MyInt(42)
print(type(n[0]))  # 4
print(n[1])  # 2

# b = '42'

# print(b[0])

# str.__getitem__()
