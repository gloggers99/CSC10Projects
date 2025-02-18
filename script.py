from datetime import datetime
from math import floor

today = datetime.now()

class User:
    __birthday_year = None
    __birthday_month = None
    __birthday_day = None

    birthday_timestamp = None

    def __init__(self, year, month, day):
        self.__birthday_year = year
        self.__birthday_month = month
        self.__birthday_day = day

        self.birthday_timestamp = datetime(self.__birthday_year, self.__birthday_month, self.__birthday_day)

    def age(self) -> int:
        return floor((today - self.birthday_timestamp).days / 365.25)

user = User(
    int(input("What year were you born in? (ex: 1990): ")),
    int(input("What month were you born in? (ex: 5): ")),
    int(input("What day were you born on? (ex: 23): ")))

print("You are " + str(user.age()) + " years old.")