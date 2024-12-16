def closure_example(x):
    """
    Реалізує функцію, яка використовує замикання для збереження значення.

    :param x: Початкове значення.
    :return: Функція, яка використовує замикання для збереження значення x.
    """
    def inner_function(y):
        nonlocal x
        x = x + y
        return x
    return inner_function


closure_instance = closure_example(5)
result = closure_instance(3)

print(result)

re = closure_instance(5)
print(re)

# Перевірка
assert closure_instance(3) == 8












