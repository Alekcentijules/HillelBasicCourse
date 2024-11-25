import string

# print(string.punctuation)
user_input = input("Enter a hashtag: ")

punk = list(string.punctuation)
my_list = ["#"]


for i in user_input:
    if i in punk:
        # print("It's")
        continue
    my_list += i
title = "".join(my_list).title().replace(" ", "")
# my_str = " ".join(title).replace(" ", "").title()

if len(title) > 140:
    print(title[0:140])

else:
    print(title)











