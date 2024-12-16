def is_even(digit):
    """ Перевірка чи є парним число """
    # return (lambda d: True if d % 2 == 0 else False)(digit)
    return digit % 2 == 0

user_input_num = int(input("Enter a number: "))
result = is_even(user_input_num)

print(result)
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')



















