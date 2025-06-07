from ..models.city import City

class User:
    def __init__(self, first_name: str, *, middle_initial: str = "", last_name: str, city: City):
        self.__first_name = first_name
        self.__middle_initial = middle_initial
        self.__last_name = last_name
        self.__city = city

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def middle_initial(self):
        return self.__middle_initial

    @middle_initial.setter
    def middle_initial(self, value):
        self.__middle_initial = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    def full_name(self):
        parts = [self.first_name]
        if self.middle_initial:
            parts.append(f"{self.middle_initial}.")
        parts.append(self.last_name)
        return " ".join(parts)