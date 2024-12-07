def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

user_input_first = float(input("Enter a first num: "))
user_input_second = float(input("Enter a second num: "))
result = find_gcd(user_input_first, user_input_second)

print(result)




