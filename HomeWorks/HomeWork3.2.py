lst = [0, 1, 2, 3, 4, 5, 6]
new_lst = []

print(lst)

first_num = lst.pop(0)
last_num = lst.pop()

new_lst.append(last_num)
new_lst.extend(lst)
new_lst.append(first_num)

print(new_lst)






