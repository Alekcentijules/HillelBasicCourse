lst = [0, 1, 7, 2, 4, 8]
sum_lst = []

# 2 solutions:


# 1
if not lst:
    print(0)

else:
    for i in range(len(lst)):
        if i % 2 != 0:
            continue
        elif i % 2 == 0:
            sum_lst.append(lst[i])

    summa = sum(sum_lst)
    mul = summa * lst[-1]

    # print(sum_lst)
    # print(summa)
    print("First solution:  ", mul, '\n')


# 2

if not lst:
    print(0)

else:
    last_i = lst[-1]

    for i in range(len(lst) -1, -1, -1):
        if i % 2 != 0:
            lst.pop(i)

    summa = sum(lst)
    mul = summa * last_i

    # print(lst)
    # print(summa)
    print("Second solution: ", mul)






