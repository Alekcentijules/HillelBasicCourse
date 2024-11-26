import string

# user_input = input("Enter a number: ")

while True:
    user_input = input("Enter a number: ")

    if user_input.isdigit():
        convert = int(user_input)

        div, mod = divmod(convert, 86400)
        div2, mod2 = divmod(mod, 3600)
        div3, mod3 = divmod(mod2, 60)

        day = str(div).zfill(2)
        num = int(day[1])

        if convert >= 0 and convert < 8640000:
            if num == 0 or (num >= 5 and num <= 9) or (div >= 11 and div <= 14):
                print(f'{div} днів, {str(div2).zfill(2)}:{str(div3).zfill(2)}:{str(mod3).zfill(2)}')
                break

            elif num == 1:
                print(f'{div} день, {str(div2).zfill(2)}:{str(div3).zfill(2)}:{str(mod3).zfill(2)}')
                break

            elif num >= 2 and num <= 4:
                print(f'{div} дні, {str(div2).zfill(2)}:{str(div3).zfill(2)}:{str(mod3).zfill(2)}')
                break
        else:
            print("""Error: You're out of range!
            Please, enter a value an correct range""")

    else:
        print("""Error: You have entered an incorrect value or you're out of range!
        Please, enter a correct value and not out of range""")


# print(div, mod)
# print(div2, mod2)
# print(div3, mod3)


