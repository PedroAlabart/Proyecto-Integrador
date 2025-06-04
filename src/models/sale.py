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

    def net_price(self):
        return self.__total_price * (1 - self.__discount / 100)

    def __str__(self):
        return f"Sale[{self.__id}] - {self.__product} x{self.__quantity} to {self.__customer.full_name()}"