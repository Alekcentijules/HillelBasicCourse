lst = [0, 1, 2, 3, 4, 5, 6]

if not lst:
    print([])

elif len(lst) == 1:
    print(lst)

elif lst:
    reverse_lst = [lst[-1]] + lst[1:-1] + [lst[0]]
    print(reverse_lst)






