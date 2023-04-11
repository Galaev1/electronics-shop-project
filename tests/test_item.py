"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from item import Item

@pytest.fixture
def test_item():
    return Item("Смартфон", 10000, 20)

def test_init():
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20



def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000

def test_apply_discount(item1):
    assert item1.apply_discount() == 8000

def test_name(item1):
    item1.name = "Телефон"
    assert item1.name == "Телефон"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('./src/items.csv')
    try:
        Item.instantiate_from_csv('./src/items.csv')
    except InstantiateCSVError:
        print('Файл item.csv поврежден')
    try:
        Item.instantiate_from_csv('../src/items.csv')
    except FileNotFoundError:
        print("Отсутствует файл item.csv")