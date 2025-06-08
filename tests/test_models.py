import pytest
from .mock_data import mock_data



def test_sale_total_price(mock_data):
    
    sale = mock_data["sale"]
    sale.quantity=10
    sale.product.price=10
    sale.discount=0.5

    expected_total = sale.quantity * sale.product.price * (1 - sale.discount)
    assert sale.total_price == expected_total, f"Expected {expected_total} but got {sale.total_price}"


def test_sale_quantity_and_discount_valid(mock_data):
    sale = mock_data["sale"]
    sale.quantity= 1
    assert isinstance(sale.quantity, int)
    assert sale.quantity > 0
    assert 0 <= sale.discount <= 1

