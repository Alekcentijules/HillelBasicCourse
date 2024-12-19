def is_even(digit):
    """ Перевірка чи є парним число """
    # dig = str(digit)
    # if dig[-1] in ("0", "2", "4", "6", "8"):
    #     return True
    # else:
    #     return False

    return True if str(digit)[-1] in ("0", "2", "4", "6", "8") else False

user_input_num = input("Enter a number: ")
result = is_even(eval(user_input_num))

print(result)

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

















