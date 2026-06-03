import pytest
from classes import Ingredient


def test_ingredient_init():
    ing = Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"


def test_ingredient_str():
    ing = Ingredient("Мука", 500, "г")
    assert str(ing) == "Мука: 500.0 г"


def test_ingredient_eq():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Мука", 400, "г")
    assert ing1 == ing2

    ing3 = Ingredient("Молоко", 100, "мл")
    ing4 = Ingredient("Мука", 100, "кг")
    assert ing1 != ing3
    assert ing1 != ing4
