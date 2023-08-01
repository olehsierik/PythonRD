# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987

# def fibo():
#     counter = -1
#     lst = [0, 1]
#     while True:
#         lst.append(lst[-1] + lst[-2])
#         counter += 1
#         print(lst)
#         yield lst[counter]

def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

generator = fibo()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
