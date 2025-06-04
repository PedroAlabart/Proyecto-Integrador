from datetime import date
from city import City


class Customer:
    def __init__(self, customer_id: int, first_name: str, middle_initial: str,
                 last_name: str, city: City, address: str, birth_date: date):
        self.__id = customer_id
        self.__first_name = first_name
        self.__middle_initial = middle_initial
        self.__last_name = last_name
        self.__city = city
        self.__address = address
        self.__birth_date = birth_date

    def full_name(self):
        if self.__middle_initial:
            return f"{self.__first_name} {self.__middle_initial}. {self.__last_name}"
        return f"{self.__first_name} {self.__last_name}"

    def __str__(self):
        return f"Customer[{self.__id}]: {self.full_name()} ({self.__city})"