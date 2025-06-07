from datetime import datetime
from employee import Employee
from customer import Customer
from product import Product

class Sale:
    def __init__(self, sale_id: int, employee: Employee, customer: Customer, product: Product,
                 quantity: int, discount: float, total_price: float, sale_date: datetime,
                 transaction_number: str):
        self.__id = sale_id
        self.__employee = employee
        self.__customer = customer
        self.__product = product
        self.__quantity = quantity
        self.__discount = discount
        self.__total_price = total_price
        self.__sale_date = sale_date
        self.__transaction_number = transaction_number

    @property
    def id(self):
        return self.__id

    @property
    def employee(self):
        return self.__employee

    @employee.setter
    def employee(self, value: Employee):
        self.__employee = value

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value: Customer):
        self.__customer = value

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value: Product):
        self.__product = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        self.__quantity = value

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value: float):
        self.__discount = value

    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, value: float):
        self.__total_price = value

    @property
    def sale_date(self):
        return self.__sale_date

    @sale_date.setter
    def sale_date(self, value: datetime):
        self.__sale_date = value

    @property
    def transaction_number(self):
        return self.__transaction_number

    @transaction_number.setter
    def transaction_number(self, value: str):
        self.__transaction_number = value

    def net_price(self):
        return self.__total_price * (1 - self.__discount / 100)

    def __str__(self):
        return f"Sale[{self.__id}] - {self.__product} x{self.__quantity} to {self.__customer.full_name()}"
