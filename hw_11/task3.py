class Squares:

    def __init__(self, n):
        self.n = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            result = self.i ** 2
            self.i += 1
            return result
        else:
            raise StopIteration

# for item in Squares(10):
#     print(item)
