user_input_first_num = float(input("Enter the first number: "))
user_input_second_num = float(input("Enter the second number: "))
user_input_operator = input("Enter operator: ")

if user_input_operator == "+":
    print(f'Result: {user_input_first_num + user_input_second_num}')
elif user_input_operator == "-":
    print(f'Result: {user_input_first_num - user_input_second_num}')
elif user_input_operator == "*":
    print(f'Result: {user_input_first_num * user_input_second_num}')
elif user_input_operator == "/":
    print(f'Result: {user_input_first_num / user_input_second_num}')




