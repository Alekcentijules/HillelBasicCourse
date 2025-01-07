def add_one(some_list):
    if not some_list:
        return "Enter at least of one digit!"
    # truth_test = True if some_list else False
    # num_lst = str(some_list)
    # do_num = "".join(num_lst).replace(",", "").replace(" ", "").strip()
    # num = int(do_num.strip("[]")) + 1
    # do_lst = [n for n in str(num)]

    num = int("".join(str(el) for el in some_list).replace(",", "").replace(" ", "").strip()) + 1
    # map(str, some_list)

    # print(num)
    # return [int(s) for s in do_lst] if truth_test else "Enter at least of one digit!"
    return [int(s) for s in str(num)]

user_input_lst = input("Enter a list of numbers: ")
result = add_one(user_input_lst)

print(result)
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
















