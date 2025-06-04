from datetime import date

from city import City
class Employee:
    def __init__(self, employee_id: int, first_name: str, middle_initial: str,
                 last_name: str, gender: str, birth_date: date,
                 hire_date: date, city: City):
        self.__id = employee_id
        self.__first_name = first_name
        self.__middle_initial = middle_initial
        self.__last_name = last_name
        self.__gender = gender
        self.__birth_date = birth_date
        self.__hire_date = hire_date
        self.__city = city

    def years_of_service(self, current_date: date) -> int:
        return (current_date - self.__hire_date).days // 365

    def full_name(self):
        if self.__middle_initial:
            return f"{self.__first_name} {self.__middle_initial}. {self.__last_name}"
        return f"{self.__first_name} {self.__last_name}"

    def __str__(self):
        return f"Employee[{self.__id}]: {self.full_name()}"