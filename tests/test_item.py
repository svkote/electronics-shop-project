# tests/test_item.py
import pytest
from src.item import Item


@pytest.fixture
def setup_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    return item1, item2


def test_calculate_total_price(setup_items):
    item1, item2 = setup_items
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount(setup_items):
    item1, item2 = setup_items
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000  # скидка не применена к item2


def test_class_attributes(setup_items):
    item1, item2 = setup_items
    assert Item.pay_rate == 0.8
    assert item1 in Item.all
    assert item2 in Item.all
