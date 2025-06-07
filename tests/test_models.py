import pytest
from datetime import date, datetime
from src.models import (
    Product, Category, Sale, Country, City, Customer, Employee
)

# País de prueba
mock_country = Country(
    country_id=1,
    name="Argentina",
    code="AR"
)

# Ciudad de prueba
mock_city = City(
    city_id=1,
    name="Buenos Aires",
    zipcode="1424",
    country=mock_country
)

# Categoría de producto
mock_category = Category(
    category_id=1,
    category_name="Tecnologia"
)

# Producto de prueba
mock_product = Product(
    product_id=1,
    name="Laptop",
    price=1500,
    category=mock_category,
    modify_date=date(2025, 1, 1),
    class_type="Low",
    is_allergic=False,
    vitality_days=115,
    resistant="Yes"
)

mock_employee = Employee(employee_id=1,
                         first_name="Pedro",
                         last_name="Alabart",
                         gender="Male",
                         birth_date=date(2000, 3, 27),
                         hire_date= date(2018, 3, 27),
                         city=mock_city)

mock_customer = Customer(
    customer_id=1,
    first_name="Juan",
    last_name="Perez",
    city=mock_city,
    address="Calle 123"
)

mock_sale = Sale(
    sale_id=1,
    employee=mock_employee,
    customer=mock_customer,
    product=mock_product,
    quantity=10,
    discount=0.5,
    sale_date=datetime.now(),
    transaction_number="AABBCC01"
)

print(mock_sale)