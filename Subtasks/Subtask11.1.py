# def bubble_sort(arr):
#     for e in range(len(arr)):
#         for l in range(0, len(arr) - e - 1):
#             if arr[l] > arr[l + 1]:
#                 arr[l], arr[l + 1] = arr[l + 1], arr[l]
#
# num_list = [34, 55, 2, 4, 7, 44, 16, 83]
# bubble_sort(num_list)
#
# print(num_list)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Приклад використання
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Відсортований масив:", my_list)



# Перевірка
assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
assert bubble_sort([3, 8, 1, 7, 2, 9, 6]) == [1, 2, 3, 6, 7, 8, 9]











