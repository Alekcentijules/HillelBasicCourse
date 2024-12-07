def sum_of_digits(number):
    return int(eval("+".join(str(number).replace("-", ""))))

user_input_num = int(input("Enter a radius: "))
result = sum_of_digits(user_input_num)

print(result)

# print(eval("-4+3"))







