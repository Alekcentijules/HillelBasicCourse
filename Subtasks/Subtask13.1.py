def check_positive(value):
    if value <= 0:
        raise ValueError("Value must be positive")
    else:
        return value

# Перевірка:
check_positive(5)  # Очікуваний результат: (без виводу, так як немає помилки)

check_positive(-3)  # Очікуваний результат: ValueError: Value must be positive