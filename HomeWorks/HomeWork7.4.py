import random

def common_elements():
    first_lst = [random.randint(1, 100) for i in range(1, 50)]
    second_lst = [random.randint(1, 100) for i in range(1, 50)]

    set1 = {el for el in first_lst if el % 3 == 0}
    set2 = {el for el in second_lst if el % 5 == 0}

    return set1.intersection(set2) if set1.intersection(set2) else "There is no overlap"

result = common_elements()
print(result)
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}



















