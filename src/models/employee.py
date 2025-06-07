from datetime import date
from .city import City
from ..models_helpers import User


class Employee(User):
    def __init__(self, employee_id: int, first_name: str, last_name: str,
                 gender: str, birth_date: date, hire_date: date,
                 city: City, middle_initial: str = ""):
        super().__init__(first_name, middle_initial=middle_initial, last_name=last_name, city=city)

        if birth_date > hire_date:
            raise ValueError(f"Birth date {birth_date} cannot be after hire date {hire_date}")

        self.__id = employee_id
        self.__gender = gender
        self.__birth_date = birth_date
        self.__hire_date = hire_date

    @property
    def employee_id(self):
        return self.__id

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value: str):
        self.__gender = value

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value: date):
        self.__birth_date = value

    @property
    def hire_date(self):
        return self.__hire_date

    @hire_date.setter
    def hire_date(self, value: date):
        self.__hire_date = value

    def years_of_service(self, current_date: date) -> int:
        return (current_date - self.__hire_date).days // 365

    def __str__(self):
        return f"Employee[{self.__id}]: {self.full_name()}"
