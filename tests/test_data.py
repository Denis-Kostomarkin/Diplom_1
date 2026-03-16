"""Тестовые данные для юнит-тестов класса Burger"""

# Данные для булочки
BUN_NAME = "test bun"
BUN_PRICE = 100.0

# Данные для соуса
SAUCE_NAME = "hot sauce"
SAUCE_PRICE = 50.0
SAUCE_TYPE = "SAUCE"

# Данные для начинки
FILLING_NAME = "cutlet"
FILLING_PRICE = 150.0
FILLING_TYPE = "FILLING"

# Ожидаемые цены (вычисляются из данных выше)
PRICE_BUN_ONLY = BUN_PRICE * 2  # 200.0
PRICE_WITH_INGREDIENTS = BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE  # 400.0

# Параметры для теста get_price
PRICE_TEST_CASES = [
    (100.0, 50.0, 150.0, 400.0),
    (0.0, 0.0, 0.0, 0.0),
    (100.0, 0.0, 0.0, 200.0),
    (50.0, 25.0, 25.0, 150.0),
]

# Параметры для теста get_receipt с разными типами ингредиентов
RECEIPT_TYPE_CASES = [
    ("SAUCE", "ketchup", 50.0),
    ("FILLING", "meat", 100.0),
    ("SPECIAL", "secret sauce", 75.0),
]