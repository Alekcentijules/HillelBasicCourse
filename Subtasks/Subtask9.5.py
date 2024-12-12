def square_numbers(numbers):
    """
    Замінює кожне число у списку його квадратом.

    :param numbers: Список чисел.
    :return: Новий список з квадратами чисел.
    """
    if not numbers:
        return []

    result = [num ** 2 for num in numbers]

    return result

num_lst = [1, 2, 3, 4, 5]
result = square_numbers(num_lst)

print(result)
assert square_numbers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
assert square_numbers([0, -1, -2, -3]) == [0, 1, 4, 9]
assert square_numbers([]) == []














