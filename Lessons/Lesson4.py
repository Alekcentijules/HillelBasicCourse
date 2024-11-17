# print('11' + 1)
# print('11' - 1)


# .sort() and .reverse()

first_list = [3, 5, 4, 2, -13, 23, 6, 7, 1]
# first_list.reverse()
first_list.sort(reverse=True)
print(first_list, '\n')


# .remove()

first_list.remove(23)
print(first_list, '\n')


# .copy()

lst = first_list
lst[0] = 12
print(lst)

print(f'lst:        {id(lst)}')
print(f'first_list: {id(first_list)}', '\n')

print(f'lst:        {id(lst)}')
lst2 = first_list[:]
print(f'first_list: {id(lst2)}', '\n')

lst2[0] = 100
print(first_list)
print(lst)
print(lst2, '\n')

lst3 = [3, 2, [1, 4]]
lst4 = lst3[:]
print(lst4)

lst4[2][0] = 5
lst4[0] = 1
print(lst4)
print(lst3, '\n')

print(id(lst3[2]))
print(id(lst4[2]), '\n')


# using method

tmp = first_list.copy()
print(tmp)
print(id(tmp))
print(id(first_list), '\n')

second_list = [[1, 2, 3], [4, 5, 6]]
tmp = second_list.copy()
print(id(second_list))
print(id(tmp), '\n')

tmp[0][0] = 7
print(tmp)
print(second_list, '\n')


# .deepcopy()

import copy

lst = [[1, 2, 3], [4, 5, 6]]
tmp = copy.deepcopy(lst)
print(tmp, '\n')

tmp[0][0] = 11
print(tmp)
print(lst, '\n')


# .clear()

tmp.clear()
print(tmp, '\n')


# sys - data size

import sys

tmp = []
print(sys.getsizeof(tmp))

tmp.append(55)
print(sys.getsizeof(tmp))

tmp.append(77)
print(sys.getsizeof(tmp))

tmp.append(777)
print(sys.getsizeof(tmp))

tmp.append(1111)
print(sys.getsizeof(tmp))

tmp.append(11)
print(sys.getsizeof(tmp))


# min(), max()

print(lst)
print(min(lst))
print(max(lst))

print(min([[2, 0], [1, 3, 4]]))
print(max([[2, 0], [1, 3, 4]]), '\n')

print(min(['3', '6']))
print(min(['A', 'a']))

print(max(['3', '6']))
print(max(['A', 'a']), '\n')


# all()

print(all([1, True, 10]))
print(all([1, False, 10]), '\n')

print(all([3 > 2, True, 5 == 5]))
print(all([3 > 2, True, 5 != 5]), '\n')

if (all([3 > 2, True, 5 == 5])):
    print('Ok')

print(bool([]), '\n')


# any()

print(any([[0, True, False]]))
print(any([]))
print(all([]), '\n')

print(any([3 > 2, True, 5 == 5]))
print(any([3 > 2, True, 5 != 5]), '\n')

a = []
if a and all(a):
    print('Ok')

else:
    print('Bad')

if all(a):
    print('Ok')

else:
    print('Bad', '\n')


# Cycles

number = 1

while number <= 10:
    print(number)
    number += 1
print("End!", '\n')


# continue

number = 0

while number < 10:
    number += 1
    if number == 5:
        continue
    print(number)


lst = [1, 3, 5, 7]

while lst:
    print(len(lst), '___', lst.pop())
print(lst)
print("End!", '\n')


# brake

number = 0

while number <= 10:
    number += 1
    if number == 5:
        break
    print(number)
print('End!')
print(number, '\n')


number = 0

while True:
    number += 2
    if number >= 11: # if number >= 11: - not end cycle
        break
    print(number, '\n')


number = 0

while True:
    number += 1
    if number == 5:
        continue
    if number == 11:
        break
    print(number)
print("End!", '\n')

# else:

# number = int(input("Input positive number: "))
# i = 2
#
# while i < number: # number // 2 + 1
#     # print(i)
#     if number % i == 0:
#         print("It's not a prime number")
#         break
#     i += 1
# else:
#     print("It's a prime number")


# a = int(input('Input a: '))
# b = int(input('Input b: '))
# i = 0
#
# while i < a:
#     j = 0
#     while j < b:
#         print('*', end='')
#         j += 1
#     print()
#     i += 1


# print() functions

print(1, 2, 3, sep='', end='\n')


# cycle for

lst = [1, 3, 5, 7]
i = 0

while i < len(lst):
    l = lst[i]
    print(l)
    i += 1
print("End", '\n')


lst = [1, 3, 5, 7]

for el in lst:
    el += 5
    print(el)
print(f"First cycle: {lst}\n")

i = 0

for el in lst:
    lst[i] = el + 5
    print(el)
    i += 1
print(f"Second cycle: {lst}\n")


lst = [1, 3, 5, 7]
i = 0

while i < len(lst):
    lst[i] += 5
    i += 1
print(f"Third cycle: {lst}\n")


lst = [1, 3, 5, 7]

for i, el in enumerate(lst):
    lst[i] += 5
    print(el, i)
print(f"Fourth cycle: {lst}\n")


# range()

print(range(10))
print(list(range(10)), '\n')

import sys

print(sys.getsizeof(range(10000000)))
print(sys.getsizeof(list(range(10))), '\n')


lst = [1, 3, 5, 7]

for i in range(len(lst)):
    print(i)
    lst[i] += 5
print(lst, '\n')

print(list(range(0, -10, -1)), '\n')


import random

my_list = []

for i in range(random.randint(6, 14)):
    my_list.append(random.randint(1, 1000))
print(my_list)


summa = 0

for el in my_list:
    summa += el
print(summa, '\n')


my_list = [random.randint(1, 100) for i in range(random.randint(6, 15))]

print(my_list)
print(sum(my_list), '\n')


print(f'Random: {random.random()}')
print(f'Randrange: {random.randrange(0, 500, 5)}\n')


city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
print(f'City from list: {random.choice(city_list)}')

random.shuffle(city_list)
print(f'Shuffle: {city_list}')
random.shuffle(lst)
print(f'Shuffle: {lst}')

print(f'Shuffle: {random.shuffle(city_list)}')
print(f'Shuffle: {random.shuffle(lst)} \n')


lst = [1, 3, 5, 7, 9]

print(f'Sample: {random.sample(lst, 3)} \n')


matrix = []

for i in range(5):
    col = []
    for j in range(4):
        col.append(random.randint(0, 100))
    matrix.append(col)
print(matrix)

for lst in matrix:
    print(lst)
print('\n')

matrix = [[random.randint(1, 100) for i in range(4)] for j in range(5)]

print(matrix, '\n')


# lst = [43, 6, 44, 7]
#
# for i in range(len(lst)):
#     print(i, end=' ')
#     print(' __ ', lst[i])
#     if lst[i] == 6:
#         _ = lst.pop(i)
#     print(lst[i])
# print(lst)


lst = [43, 6, 44, 7]

for el in lst:
    print(el)
    if el == 6:
        lst.remove(6)
    print(el, '\n')


i = 0
lst = [43, 6, 44, 7]

while i < 6:
    for j in lst:
        print(j + i, end=" ")
    print()
    i += 1


