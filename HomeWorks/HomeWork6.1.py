import string

letters = string.ascii_letters
# print(letters)
user_input = input("Enter the desired range of letters: ")

# indexes = [i for i in range(len(letters))]
# print(indexes)


# for l in user_input:
#     if l in letters:
#         for l in range(len(letters)):
#             indexes.append(l)
#             print(indexes)
#         # lst.append(letters[l])
#     # elif l is "-":
#     #     lst.append(letters[user_input[0]], )
# for i in range(len(letters)):
#     indexes.append(i)
# print(indexes)

# for let in user_input:
#     if let in letters:
#         letters[let]



# print(indexes)



my_letters = []
start_letter = user_input[0]
end_letter = user_input[2]

start_index = letters.index(start_letter)
end_index = letters.index(end_letter)


# Version 1
for let in range(start_index, end_index):
    if let in range(len(letters)):
        my_letters.append(letters[let])
        # my_letters.append(end_letter)

my_letters.append(end_letter)
result = "".join(my_letters)

# print(start_index, end_index)
print(f'Version 1: {result} \n')



# Version 2
result = letters[start_index: end_index + 1]

print(f'Version 2: {result}')