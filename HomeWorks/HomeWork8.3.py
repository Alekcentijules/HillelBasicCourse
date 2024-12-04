def find_unique_value(some_list):
    uniq_num = [num for num in some_list if some_list.count(num) < 2]
    if not uniq_num:
        return "No unique number was found..."

    return int(uniq_num[0]) if uniq_num and uniq_num[0].is_integer() else uniq_num[0]

user_input_num = input("Enter a list of numbers: ")
if user_input_num:
    user_input_num_lst = [float(num) for num in user_input_num.split(",")]
    result = find_unique_value(user_input_num_lst)
    print(result)

else: print("Error: The conversation requires at least one number!")

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
















