def multiply_even_numbers(numbers):
    """
    Помножує всі парні числа у списку на 2.

    :param numbers: Список чисел.
    :return: Новий список з парними числами, помноженими на 2.
    """

    if not numbers:
        return f"The list is blank!\n Please enter at least one number."

    numb = []
    result = [num if not num % 2 == 0 else numb.append(num * 2) for num in numbers]

    return numb

result = multiply_even_numbers([1, 2, 3, 4, 5, 6])

print(result)
assert multiply_even_numbers([1, 2, 3, 4, 5, 6]) == [4, 8, 12]














