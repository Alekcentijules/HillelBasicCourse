import keyword
import string

# keyw = keyword.kwlist

# print(not_use_this_words)
# w = []

# for word in keyword.kwlist:
#     w.append(word)
# print(w)
#
# not_use_this_words = [w[el] for el in range(1,-1)]
# dgt = string.digits
# not_use = [dgt[el] for el in range(1,-1)]


user_input = input("Enter a variable: ")
invalid_characters = list(string.punctuation.replace("_", "") + " ")
is_valid = True

# _ = lst.pop(26)
# print(lst)
# # print(_)



if keyword.iskeyword(user_input):
    is_valid = False

elif user_input[0].isdigit():
    is_valid = False

elif user_input.startswith("_") or user_input.endswith("_"):
    is_valid = False

elif "__" in user_input:
    is_valid = False

# elif user_input.count("_") > 1:
#     if user_input.lstrip("_"):
#         is_valid = False
#
#     elif user_input.rstrip("_"):
#         is_valid = False


for letter in user_input:
    if letter in string.ascii_uppercase:
        is_valid = False

    if letter in invalid_characters:
        is_valid = False

    # else:
    #     print(True)

print(is_valid)










