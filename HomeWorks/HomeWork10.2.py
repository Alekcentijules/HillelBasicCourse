import string


def first_word(text):
    """ Пошук першого слова """
    punk = string.punctuation.replace("'", "").replace(" ", "")
    del_punc = [i.replace(i, " ") if i in punk else i for i in text]
    words = "".join(del_punc).strip().split()

    return words[0]

user_input = input("Enter a text: ")
result = first_word(user_input)

print(result)
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')















