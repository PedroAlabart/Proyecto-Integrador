import pytest
from datetime import date, datetime
from src.models import (
    Product, Category, Sale, Country, City, Customer, Employee
)

@pytest.fixture
def mock_data():
    country = Country(country_id=1, name="Argentina", code="AR")
    city = City(city_id=1, name="Buenos Aires", zipcode="1424", country=country)
    category = Category(category_id=1, category_name="Tecnologia")
    product = Product(
        product_id=1,
        name="Laptop",
        price=1500,
        category=category,
        modify_date=date(2025, 1, 1),
        class_type="Low",
        is_allergic=False,
        vitality_days=115,
        resistant="Durable"
    )
    employee = Employee(
        employee_id=1,
        first_name="Pedro",
        last_name="Alabart",
        gender="Male",
        birth_date=date(2000, 3, 27),
        hire_date=date(2018, 3, 27),
        city=city
    )
    customer = Customer(
        customer_id=1,
        first_name="Juan",
        last_name="Perez",
        city=city,
        address="Calle 123"
    )
    sale = Sale(
        sale_id=1,
        employee=employee,
        customer=customer,
        product=product,
        quantity=10,
        discount=0.5,
        sale_date=datetime.now(),
        transaction_number="AABBCC01"
    )
    return {
        "country": country,
        "city": city,
        "category": category,
        "product": product,
        "employee": employee,
        "customer": customer,
        "sale": sale
    }