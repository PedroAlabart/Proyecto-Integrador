class Category:
    def __init__(self, category_id: int, category_name: str):
        self.__id = category_id
        self.__name = category_name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Category[{self.__id}]: {self.__name}"