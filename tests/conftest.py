"""Фикстуры для тестов класса Burger"""

import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger  
from tests.test_data import (
    BUN_NAME, BUN_PRICE,
    SAUCE_NAME, SAUCE_PRICE, SAUCE_TYPE,
    FILLING_NAME, FILLING_PRICE, FILLING_TYPE
)


@pytest.fixture
def burger():
    """Создает пустой бургер"""
    return Burger()  


@pytest.fixture
def mock_bun():
    """Мок булочки с данными из test_data"""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = BUN_NAME
    bun.get_price.return_value = BUN_PRICE
    return bun


@pytest.fixture
def mock_sauce():
    """Мок соуса с данными из test_data"""
    sauce = Mock(spec=Ingredient)
    sauce.get_name.return_value = SAUCE_NAME
    sauce.get_price.return_value = SAUCE_PRICE
    sauce.get_type.return_value = SAUCE_TYPE
    return sauce


@pytest.fixture
def mock_filling():
    """Мок начинки с данными из test_data"""
    filling = Mock(spec=Ingredient)
    filling.get_name.return_value = FILLING_NAME
    filling.get_price.return_value = FILLING_PRICE
    filling.get_type.return_value = FILLING_TYPE
    return filling