def init():
    dct = {}
    return dct


def add_to_dict(dct, key, value):
    dct[key] = value


dct = init()

print(dct)
# others = {"C++": "Bjarne Stroustrup"}
# dct.update(others)

add_to_dict(dct,'C++','Bjarne Stroustrup')

print(dct)