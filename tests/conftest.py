"""Фикстуры для тестов класса Burger"""

import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    """Создает пустой бургер"""
    from praktikum.burger import Burger
    return Burger()


@pytest.fixture
def mock_bun():
    """Мок булочки"""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "test bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_sauce():
    """Мок соуса"""
    sauce = Mock(spec=Ingredient)
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 50.0
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return sauce


@pytest.fixture
def mock_filling():
    """Мок начинки"""
    filling = Mock(spec=Ingredient)
    filling.get_name.return_value = "cutlet"
    filling.get_price.return_value = 150.0
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    return filling