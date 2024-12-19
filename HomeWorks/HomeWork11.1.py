def prime_generator(end):
    # num_lst = []
    for num in range(2, end + 1):
        # if (not num <= 1) and (num == 2 or num == 3) and (not num % 2 == 0 and not num % 3 == 0):
        #     num_lst.append(num)
        #     yield num_lst
        is_true = True
        for n in range(2, int(num**0.5) + 1):
            if num % n == 0:
                is_true = False
                break

        if is_true:
            # num_lst.append(num)
            yield num

from inspect import isgenerator

test_gen = prime_generator(15)
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))

gen = prime_generator(15)

assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

















