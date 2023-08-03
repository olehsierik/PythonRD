def fibo_sequence(n):
    counter = 0
    lst = [0, 1]
    while n > counter:
        lst.append(lst[-1] + lst[-2])
        yield lst[counter]
        counter += 1


for item in fibo_sequence(11):
    print(item)
