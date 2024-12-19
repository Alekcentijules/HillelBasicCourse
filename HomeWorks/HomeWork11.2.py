def generate_cube_numbers(end):
    # for num in range(2, end):
    #     cube = num ** 3
    #     if cube <= end:
    #         yield cube
    yield from (num ** 3 for num in range(2, end) if num ** 3 <= end)

from inspect import isgenerator

gen = generate_cube_numbers(1000)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


gen = generate_cube_numbers(10)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

















