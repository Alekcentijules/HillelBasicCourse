# user_input_first_num = float(input("Enter the first number: "))
# user_input_second_num = float(input("Enter the second number: "))
# user_input_operator = input("Enter operator: ")
# attempts = [1]
# is_valid = True
# user_input_agreement = input("Do you like to continue? \n Please enter 'Yes/y' or 'No/n': ")

while True:
    # user_input_agreement = input("Do you like to continue? \n Please enter 'Yes/y' or 'No/n': ")

    while True:
        user_input_first_num = input("Enter the first number: ")

        if user_input_first_num.count("-") > 1 or (user_input_first_num[0] == "-" and user_input_first_num[1:].count("-") > 0):
            print("Error: Please enter a valid number")
            continue

        elif user_input_first_num.replace(".", "").isdigit() or (user_input_first_num[0] == "-" and user_input_first_num[1:].replace(".", "", 1).isdigit()):
            user_input_first_num = float(user_input_first_num)
            break

        else:
            print("Error: Please enter a valid number")




    while True:
        user_input_second_num = input("Enter the second number: ")

        if user_input_second_num.count("-") > 1 or (user_input_second_num[0] == "-" and user_input_second_num[1:].count("-") > 0):
            print("Error: Please enter a valid number")
            continue

        elif user_input_second_num.replace(".", "").isdigit() or (user_input_second_num[0] == "-" and user_input_second_num[1:].replace(".", "", 1).isdigit()):
            user_input_second_num = float(user_input_second_num)
            break

        else:
            print("Error: Please enter a valid number")



    while True:
        user_input_operator = input("Enter operator: ")

        if user_input_operator == "+":
            print(f'Result: {user_input_first_num + user_input_second_num}')
            break

        elif user_input_operator == "-":
            print(f'Result: {user_input_first_num - user_input_second_num}')
            break

        elif user_input_operator == "*":
            print(f'Result: {user_input_first_num * user_input_second_num}')
            break

        elif user_input_operator == "/":
            if user_input_second_num != 0:
                print(f'Result: {user_input_first_num / user_input_second_num}')
                break

            else:
                print("Error: Division by zero is not allowed!")


        else:
            print("Error: Invalid operator entered. Please use +, -, *, or /")



    while True:
        user_input_agreement = input("Do you like to continue? \n Please enter 'Yes/y' or 'No/n': ").strip().lower()

        if user_input_agreement in ["yes", "y"]:
            break

        elif user_input_agreement in ["no", "n"]:
            print("""Thank you for using our programme.
        And to keep you from getting bored we 
        leave you with our philosophy to read. 
        Share your thoughts after reading it: \n
        Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested. 
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!""")
            break

        else:
            print("Error: Please enter the correct value!")


    if user_input_agreement in ["no", "n"]:
        break




