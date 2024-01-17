"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    item1.pay_rate = 0.5
    assert item1.apply_discount() == 5000


def test_name_getter():
    assert item1.name == 'Смартфон'


def test_name_setter():
    assert item1.name == 'Смартфон'
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_repr():
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    assert str(item1) == 'Смартфон'
