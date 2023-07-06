from dateutil.parser import parse as du_parse
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from datetime import date

d1 = date.fromisoformat('1993-12-07')
d2 = date.today()
delta = relativedelta(d2, d1)

y = delta.years * 12 + delta.months

print(y)

my_name='Oleh'
my_age = 25

print("dd" + my_name + " " + str(my_age) + " " + str(my_age))


# print('Start')
# res = input("Enter your age: ")
# if res.isnumeric():
#     res = int(res)
#     if res >= 18:
#         print(f'You are adult. Your age is {res}')
#     else:
#         print(f'You are too young. Your age is {res}')
# else:
#     print('Entered value is invalid')
# print('End')