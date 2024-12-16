def repeat_decorator(repeat_count):
    """
    Реалізує декоратор, який повторює виклик функції задану кількість разів.

    :param repeat_count: Кількість повторень.
    :return: Декоратор для повторюваного виклику функції.
    """
    def innit_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(repeat_count):
                func(*args, **kwargs)
            return None
        return wrapper
    return innit_decorator
@repeat_decorator(3)
def example_function():
    print("Repeat")

example_function()
# Перевірка
# assert example_function() is None













