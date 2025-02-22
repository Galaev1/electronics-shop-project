"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from phone import Phone
from src.item import Item


@pytest.fixture()
def item1():
    return Item("Смартфон", 10000, 20)


def test_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    assert item1.apply_discount() == 10000


def test_name(item1):
    item1.name = "Телефон"
    assert item1.name == "Телефон"


def test_instantiate_from_csv(item1):
    return item1.instantiate_from_csv()

def test_add_isinstance():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
