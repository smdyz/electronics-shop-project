"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone

item1 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_repr():
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    assert str(item1) == 'Смартфон'
    assert str(phone1) == 'iPhone 14'


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    item1.pay_rate = 0.5
    assert item1.apply_discount() == 5000


def test_string_to_num():
    assert Item.string_to_number('5.0') == 5


def test_name_getter():
    assert item1.name == 'Смартфон'


def test_name_setter():
    assert item1.name == 'Смартфон'
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_add():
    assert item1 + phone1 == 25
    assert phone1 + 1 is None


def test_number_of_sim():
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0

