from country import Country

class City:
    def __init__(self, city_id: int, name: str, zipcode: str, country: Country):
        self.__id = city_id
        self.__name = name
        self.__zipcode = zipcode
        self.__country = country

    def __str__(self):
        return f"{self.__name}, {self.__country}"