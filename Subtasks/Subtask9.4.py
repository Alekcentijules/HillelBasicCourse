def factorial(num):
    """
    Обчислює факторіал числа num.

    :param n: Ціле число.
    :return: Факторіал числа num.
    """
    if num == 1:
        return num

    return num * factorial(num - 1)

user_input_num = int(input("Enter a number: "))
result = factorial(user_input_num)

print(result)
assert factorial(5) == 120