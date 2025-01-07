# import string

user_input = input("Enter a number: ")

# if user_input.isdigit():
#     num_list = list(user_input)
#     result = 0
#     if len(user_input)
#     div, mod = divmod(convert, )
#     while user_input <= 9:
#     for num in range(len(user_input)):
#     divider = "1".zfill(zero_count)
#     zero_count = user_input.count("") - 1
#     zero = user_input.replace(string.digits, "0")
#
#
#     count_of_num = user_input.count("") - 1
#     zero = "".join("0" if char.isdigit() else char for char in user_input).replace("0", "", 1)
#     divider = f"1{zero}"
#     converter1, converter2 = int(user_input), int(divider)
#
#
#     print(count_of_num)
#
#     div_mod = []
#
#     while count_of_num > 1:
#         div, mod = divmod(converter1, converter2)
#         print(div, mod)
#
#         count_of_num -= 1
#
#     for num in user_input:
#
#
#
#
#     print(div_mod)
#
#     print(divider)
#     print(zero_count)
#     print(zero)



if not user_input.isdigit():
    print("""Error: You have entered an incorrect value or you're out of range!
                            Please, enter a correct value and not out of range""")

digits = int(user_input)

while digits > 9:
    product = 1

    for num in str(digits): # not user_input
        product *= int(num)
    digits = product

print(digits)


# Version 2

digit = input("Enter a number: ")

while len(digit) > 1:
    tmp = "*".join(digit)
    digit = str(eval(tmp))

print(digit)




