from city import City
from models_helpers.abstracts import User

class Customer(User):
    def __init__(self, customer_id: int, first_name: str, middle_initial: str,
                 last_name: str, city: City, address: str):
        super().__init__(first_name, middle_initial, last_name, city)
        self.__id = customer_id
        self.__city = city
        self.__address = address

    # id solo getter
    @property
    def id(self):
        return self.__id

    # city getter y setter
    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    # address getter y setter
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    def __str__(self):
        return f"Customer[{self.__id}]: {self.full_name()} ({self.__city})"
    