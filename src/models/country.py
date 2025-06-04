
class Country:
    def __init__(self, country_id: int, name: str, code: str):
        self.__id = country_id
        self.__name = name
        self.__code = code

    def __str__(self):
        return f"{self.__name} ({self.__code})"