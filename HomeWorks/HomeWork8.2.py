import string

def is_palindrome(text):
    punk = list(string.punctuation)
    palin = "".join(el for el in text if (el not in punk and not el.isdigit()) and not el == " ").lower()

    return True if palin == palin[::-1] else False

user_input_palindrome = input("Enter a string palindrome: ")

print(is_palindrome(user_input_palindrome))
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
print("ОК")






















