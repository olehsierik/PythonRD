from dateutil.relativedelta import relativedelta
from datetime import date

d1 = date.fromisoformat('1993-12-07')
d2 = date.today()
delta = relativedelta(d2, d1)

age_in_month = delta.years * 12 + delta.months

age_in_years = int(age_in_month / 12)

my_name = 'Oleh'

my_age = ("Му name is " + str(my_name) + ", I am " + str(age_in_years) + " years old.")

# print(age_in_month)
# print(age_in_years)
# print(my_name)
# print(my_age)
