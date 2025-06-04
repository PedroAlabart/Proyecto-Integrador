from datetime import date, datetime
from category import Category

class Product:
    def __init__(self, product_id: int, name: str, price: float, category: Category,
                 class_type: str, modify_date: date, resistant: str,
                 is_allergic: str, vitality_days: float):
        self.__id = product_id
        self.__name = name
        self.__price = price
        self.__category = category
        self.__class_type = class_type
        self.__modify_date = modify_date
        self.__resistant = resistant
        self.__is_allergic = is_allergic
        self.__vitality_days = vitality_days

    def is_expired(self, current_date: date) -> bool:
        days_elapsed = (current_date - self.__modify_date).days
        return days_elapsed > self.__vitality_days

    def __str__(self):
        return f"{self.__name} (${self.__price})"
