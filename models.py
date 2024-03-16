from datetime import datetime


class Employee:
    def __init__(self, fullname, birth_date, gender):
        self.fullname: str = fullname
        self.birth_date: datetime = birth_date
        self.gender: str = gender

    def calculate_age(self):
        today = datetime.now()
        age = today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

# ivan = Employee("Ivan Jovanovich Ivanov", datetime(2000, 1, 16), Gender.Male)
# print(ivan.calculate_age())
# print(ivan.gender)
