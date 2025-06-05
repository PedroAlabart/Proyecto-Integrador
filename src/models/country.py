class Country:
    def __init__(self, country_id: int, name: str, code: str):
        self.__id = country_id
        self.__name = name
        self.__code = code

    # Getter para id (sin setter)
    @property
    def id(self):
        return self.__id

    # Getter y setter para name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # Getter y setter para code
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value

    def __str__(self):
        return f"{self.__name} ({self.__code})"
