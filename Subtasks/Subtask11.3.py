def linear_search(arr, target):
    for el in range(len(arr)):
        if arr[el] == target:
            return el
    return -1

print(linear_search([64, 34, 25, 12, 22, 11, 90], 11))

# Перевірка
assert linear_search([64, 34, 25, 12, 22, 11, 90], 22) == 4

















