from datetime import datetime
from .employee import Employee
from .customer import Customer
from .product import Product

class Sale:
    def __init__(self, sale_id: int, employee: Employee, customer: Customer, product: Product,
                 quantity: int, discount: float,sale_date: datetime,
                 transaction_number: str):
        
        if  quantity < 1:
            raise ValueError("La cantidad debe ser un numero positivo")
        if not(0 <= discount <= 1):
            raise ValueError("El descuento debe estar entre 0 y 1")


        self.__id = sale_id
        self.__employee = employee
        self.__customer = customer
        self.__product = product
        self.__quantity = quantity
        self.__discount = discount
        self.__sale_date = sale_date
        self.__transaction_number = transaction_number

    @property
    def total_price(self):
        return self.quantity * self.product.price * (1 - self.discount)

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
        if value <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.__quantity = value

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value: float):
        self.__discount = value


    @property
    def sale_date(self):
        return self.__sale_date

    @sale_date.setter
    def sale_date(self, value: datetime):
        self.__sale_date = value

    @property
    def transaction_number(self):
        return self.__transaction_number


    def __str__(self):
        return f"Sale[{self.__id}] - {self.__product} x{self.__quantity} to {self.__customer.full_name()}"
