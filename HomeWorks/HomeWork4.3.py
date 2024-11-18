import random

lst = [random.randint(1, 100) for i in range(random.randint(3, 10))]
# lst = [1, 2, 3, 4, 5, 6, 7, 9]
new_lst = []


# if not lst:
#     print([])
#
# elif len(lst) < 2:
#     print(lst)
#
# elif:


#version 1
for i in range(len(lst)):
    if i == 0:
        new_lst.append(lst[i])
    elif i == 2:
        new_lst.append(lst[i])

penultimate_el = [lst[el] for el in range(len(lst) -1, -1, -1)]
p = [penultimate_el.pop(1)]

print("Version 1: ", new_lst + p, '\n')




#version 2
new_lst = [lst[0], lst[2], lst[-2]]

print("Version 2: ", new_lst)





















