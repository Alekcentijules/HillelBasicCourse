import operator

def calculator(num1, num2, operation):
    # import operator
    """
    Реалізує простий калькулятор для двох чисел.

    :param num1: Перше число.
    :param num2: Друге число.
    :param operation: Операція (додавання, віднімання, множення, ділення).
    :return: Результат операції.
    """

    operators = {"+": operator.add,
           "-": operator.sub,
           "*": operator.mul,
           "/": operator.truediv,
           "//": operator.floordiv,
           "**": operator.pow,
           "%": operator.mod
           }

    if num2 == 0 and operation in ["/", "//", "%"]:
        return "Error: You can't divide by 0!"

    if operation not in operators:
        return "Error: You need to enter the correct operation!"

    result = operators.get(operation)

    return result(num1, num2)

u_i_x = float(input("Enter the first number: "))
u_i_op = input("Enter a operation: ")
u_i_y = float(input("Enter the second number: "))
result = calculator(u_i_x, u_i_y, u_i_op)

print(result)

assert calculator(5, 3, '+') == 8