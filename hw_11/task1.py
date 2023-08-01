class Numbers():
    n = -1

    def __next__(self):
        self.n += 1
        return self.n


# number_iterator = Numbers()
# print(next(number_iterator))  # 0
# print(next(number_iterator))  # 1
# print(next(number_iterator))  # 2
#
#
# while True:
#     print(next(number_iterator))
#

