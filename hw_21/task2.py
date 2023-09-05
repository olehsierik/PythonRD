import random
import string


class User:

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __add__(self, other):
        child_age = 0

        child_first_name = random.choice(string.ascii_uppercase) + "".join(
            random.choices(string.ascii_lowercase, k=random.randint(1, 9)))

        if self.age == other.age or self.age > other.age:
            child_last_name = self.last_name
        else:
            child_last_name = other.last_name

        return User(child_first_name, child_last_name, child_age)

    def __eq__(self, other):
        return self.first_name.lower()==other.first_name.lower()

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __lt__(self, other):
        return self.age < other.age


user1 = User(first_name="Oleksii", last_name="Klymenok", age=32)
user2 = User(first_name="Oleksii", last_name="Testenko", age=25)
user3 = user1 + user2

print(f"{user3.first_name} {user3.last_name}: {user3.age}")

print(user1 > user2) # True
print(user1 >= user2) # True
print(user1 < user2) # False
print(user1 <= user2) # False
print(user1 == user2) # True