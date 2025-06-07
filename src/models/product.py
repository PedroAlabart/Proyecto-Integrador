from datetime import date
from .category import Category
from ..models_helpers.data_types import ClassDataType, ResistantDataType

class Product:
    def __init__(self, product_id: int, name: str, price: float, category: Category,
                 class_type: str, modify_date: date, resistant: str,
                 is_allergic: bool, vitality_days: int):

        self.__id = product_id
        self.__name = name
        self.__price = price
        self.__category = category
        self.__class_type = ClassDataType(class_type)
        self.__modify_date = modify_date
        self.__resistant = ResistantDataType(resistant)
        self.__is_allergic = is_allergic
        self.__vitality_days = vitality_days

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
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        self.__price = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value: Category):
        self.__category = value

    @property
    def class_type(self):
        return self.__class_type

    @class_type.setter
    def class_type(self, value: str):
        self.__class_type = value

    @property
    def modify_date(self):
        return self.__modify_date

    @modify_date.setter
    def modify_date(self, value: date):
        self.__modify_date = value

    @property
    def resistant(self):
        return self.__resistant

    @resistant.setter
    def resistant(self, value: str):
        self.__resistant = value

    @property
    def is_allergic(self):
        return self.__is_allergic

    @is_allergic.setter
    def is_allergic(self, value: str):
        self.__is_allergic = value

    @property
    def vitality_days(self):
        return self.__vitality_days

    @vitality_days.setter
    def vitality_days(self, value: float):
        self.__vitality_days = value

    def __str__(self):
        return f"{self.__name} (${self.__price})"
