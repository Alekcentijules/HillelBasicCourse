a = None
b = 0
c = b or a
d = a or b

print(c)
print(d)

if bool(b):
    c = b
else:
    c = a

print(c)

if a:
    print("a not = 0")
elif not a:
    print("a = 0")


# num_b = int(input("Enter num b: "))
# num_a = 10 if num_b < 5 else 20
#
# print(num_a)


lst = list("Hello, Jonny!")

print(lst)


first_list = [2, 3, 4, 5, 6, 1]
first_list.insert(5, 7)

print(first_list)


first_list.insert(11, 11)

print(first_list)


del(first_list[0])

print(first_list)


pip = first_list.pop()
pap = first_list.pop(3)

print(pip)
print(pap)
print(first_list)
print(54 in first_list, "\n")


second_lst = [[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]]

print(len(second_lst[0]), "\n")


first_list.extend([22, 33, 55, 66, 77])

print(first_list)

first_list.append(22)

print(first_list)

first_list.append([22, 33, 55, 66, 77])

print(first_list, "\n")


l = first_list.append(99)

print(l, "\n")


lst = [[0, 0, 0]] * 3
print(lst)

lst[0][0] = 32
lst[2][2] = 66

print(lst)


lst = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
lst[0][0] = 32
lst[2][2] = 66

print(lst, "\n")


my_list = first_list[3:10:2]

print(my_list)

my_list = first_list[3:-1]

print(my_list)
print(my_list[::-1])