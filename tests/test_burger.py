"""Юнит-тесты для класса Burger с использованием моков и параметризации"""

import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from test_data import (
    BUN_NAME, BUN_PRICE,
    SAUCE_NAME, SAUCE_PRICE, SAUCE_TYPE,  
    PRICE_BUN_ONLY, PRICE_WITH_INGREDIENTS,
    PRICE_TEST_CASES,
    RECEIPT_TYPE_CASES,
    FILLING_NAME
)


class TestBurger:

    # =========== Тесты для set_buns ===========

    def test_set_buns_sets_bun(self, burger, mock_bun):
        """Проверяет, что метод set_buns устанавливает булочку"""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # =========== Тесты для add_ingredient ===========

    def test_add_ingredient_adds_one_ingredient(self, burger, mock_sauce):
        """Проверяет добавление одного ингредиента"""
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce

    def test_add_ingredient_adds_multiple_ingredients(self, burger, mock_sauce, mock_filling):
        """Проверяет добавление нескольких ингредиентов"""
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert len(burger.ingredients) == 2

    # =========== Тесты для remove_ingredient ===========

    def test_remove_ingredient_removes_by_index(self, burger, mock_sauce, mock_filling):
        """Проверяет удаление ингредиента по индексу"""
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_filling

    def test_remove_ingredient_invalid_index_raises_error(self, burger):
        """Проверяет, что удаление по неверному индексу вызывает IndexError"""
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    # =========== Тесты для move_ingredient ===========

    @pytest.mark.parametrize("index,new_index,expected_first,expected_second", [
        (0, 1, "second", "first"),
        (1, 0, "second", "first"),
    ])
    def test_move_ingredient_moves_correctly(self, burger, index, new_index, expected_first, expected_second):
        """Параметризованный тест перемещения ингредиентов"""
        first = Mock()
        first.get_name.return_value = "first"
        
        second = Mock()
        second.get_name.return_value = "second"
        
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        
        burger.move_ingredient(index, new_index)
        
        assert burger.ingredients[0].get_name() == expected_first
        assert burger.ingredients[1].get_name() == expected_second

    # =========== Тесты для get_price ===========

    def test_get_price_without_bun_raises_error(self, burger, mock_sauce):
        """Проверяет, что при отсутствии булочки вызывается ошибка"""
        burger.add_ingredient(mock_sauce)
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_price_with_bun_no_ingredients(self, burger, mock_bun):
        """Проверяет цену только с булочкой (без ингредиентов)"""
        burger.set_buns(mock_bun)
        assert burger.get_price() == PRICE_BUN_ONLY

    def test_get_price_with_ingredients(self, burger, mock_bun, mock_sauce, mock_filling):
        """Проверяет цену с булочкой и ингредиентами"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == PRICE_WITH_INGREDIENTS

    @pytest.mark.parametrize("bun_price,sauce_price,filling_price,expected", PRICE_TEST_CASES)  
    def test_get_price_parametrized(self, burger, bun_price, sauce_price, filling_price, expected):
        """Параметризованный тест расчета цены с разными ценами"""
        bun = Mock()
        bun.get_price.return_value = bun_price
        
        sauce = Mock()
        sauce.get_price.return_value = sauce_price
        
        filling = Mock()
        filling.get_price.return_value = filling_price
        
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        
        assert burger.get_price() == expected

    # =========== Тесты для get_receipt ===========

    def test_get_receipt_format(self, burger, mock_bun, mock_sauce, mock_filling):
        """Проверяет формат чека - использует данные из test_data"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        
        receipt = burger.get_receipt()
        lines = receipt.split('\n')
        
        assert lines[0] == f"(==== {BUN_NAME} ====)"
        assert lines[1] == f"= sauce {SAUCE_NAME} ="
        assert lines[2] == f"= filling {FILLING_NAME} ="
        assert lines[3] == f"(==== {BUN_NAME} ====)"
        assert lines[4] == ""
        assert f"Price: {PRICE_WITH_INGREDIENTS}" in lines[5]

    def test_get_receipt_contains_all_data(self, burger, mock_bun, mock_sauce):
        """Проверяет, что чек содержит все необходимые данные"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        
        receipt = burger.get_receipt()
        
        assert BUN_NAME in receipt
        assert SAUCE_TYPE.lower() in receipt
        assert SAUCE_NAME in receipt
        assert "Price:" in receipt

    @pytest.mark.parametrize("ingredient_type,ingredient_name,ingredient_price", RECEIPT_TYPE_CASES)  
    def test_get_receipt_different_ingredient_types(self, burger, mock_bun, ingredient_type, ingredient_name, ingredient_price):
        """Параметризованный тест чека с разными типами ингредиентов"""
        ingredient = Mock()
        ingredient.get_name.return_value = ingredient_name
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_price.return_value = ingredient_price
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(ingredient)
        
        receipt = burger.get_receipt()
        
        assert ingredient_name in receipt
        assert ingredient_type.lower() in receipt
        assert "Price:" in receipt