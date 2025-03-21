def calculate_sell(sell):
    """
    Обчислює загальний дохід для кожного продукту.
    Args:
        продажі: Список словників, де кожен словник представляє продаж з ключами "продукт", "кількість", "ціна".
    Returns:
        Словник, де ключі - це назви продуктів, а значення - загальний дохід.
    """
    total_value = {}
    for item in sell:
        good_name = item["продукт"]
        quantity = item["кількість"]
        price = item["ціна"]
        value = quantity * price
        if good_name in total_value:
            total_value[good_name] += value
        else:
            total_value[good_name] = value
    return total_value

# Приклад використання
sell = [
    {"продукт": "яблуко", "кількість": 10, "ціна": 5},
    {"продукт": "банан", "кількість": 20, "ціна": 3},
    {"продукт": "яблуко", "кількість": 5, "ціна": 5},
    {"продукт": "яблуко", "кількість": 50, "ціна": 100},
    {"продукт": "апельсин", "кількість": 15, "ціна": 4},
    {"продукт": "банан", "кількість": 100, "ціна": 10}
]

total_sell_value = calculate_sell(sell)
print("Загальний дохід за продуктом:", total_sell_value)

# Створення списку продуктів, що принесли дохід більший ніж 1000
list_for_goods = []

for good in total_sell_value:
    print("key:", good)
    print("value", total_sell_value[good])
    if total_sell_value[good] > 1000:
        list_for_goods.append(good)

print("Продукти з доходом більше 1000:", list_for_goods)