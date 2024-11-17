lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
nn = []
z = []
i = 0

# not work
# for el in range(len(lst)):
#     if lst[el] == 0:
#         lst.pop(el)
#         lst.append(0)
#
# print(lst)



# 2 solutions:


#1
for el in range(len(lst)):
    if lst[el] > 0:
        nn.append(lst[el])
    elif lst[el] == 0:
        z.append(lst[el])

new_list = nn + z
print("First solution:  ", new_list, '\n')


#2
for i in range(len(lst) -1, -1, -1):
    if lst[i] == 0:
        lst.pop(i)
        lst.append(0)

print("Second solution: ", lst)





















