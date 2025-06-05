from country import Country

class City:
    def __init__(self, city_id: int, name: str, zipcode: str, country: Country):
        self.__id = city_id
        self.__name = name
        self.__zipcode = zipcode
        self.__country = country

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def zipcode(self):
        return self.__zipcode

    @zipcode.setter
    def zipcode(self, value: str):
        self.__zipcode = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value: Country):
        self.__country = value

    def __str__(self):
        return f"{self.__name}, {self.__country}"