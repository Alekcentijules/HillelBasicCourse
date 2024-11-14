lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_lst = []

if len(lst) % 2 == 0:
    part = len(lst) // 2
    new_lst.append(lst[:part])
    new_lst.append(lst[part:])
    print(new_lst)

elif len(lst) % 2 != 0:
    part = len(lst) // 2 + 1
    new_lst.append(lst[:part])
    new_lst.append(lst[part:])
    print(new_lst)











