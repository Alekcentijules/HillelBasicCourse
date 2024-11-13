lst = [0, 1, 2, 3, 4, 5]

print(lst)

if not lst:
    print([])

elif lst:
    reverse_lst = [lst[-1]] + lst[0:-1]
    print(reverse_lst)






